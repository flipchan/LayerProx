#!/usr/bin/env python
# coding: utf-8

import scrypt
password = 'abc123uj'
from base64 import b64encode, b64decode
import sys, os
import marionette_tg.conf
password = marionette_tg.conf.get("crypt.scrypt")
home = marionette_tg.conf.get("crypt.clienthomedir")
clientkey = marionette_tg.conf.get("crypt.clientkey")
serverkey = marionette_tg.conf.get("crypt.serverkey")
clientpassword = marionette_tg.conf.get("crypt.clientpassword")
serverpassword = marionette_tg.conf.get("crypt.serverpassword")

import gnupg
gpg = gnupg.GPG(homedir=home)# gpg home
gpg.encoding = 'utf-8'

#p = marionette_tg.conf.get('server.s')
import math

import fte.encoder
import marionette_tg.record_layer

MAX_CELL_LENGTH_IN_BITS = (2 ** 18) * 8


def send_async(channel, marionette_state, input_args):
    send(channel, marionette_state, input_args, blocking=False)
    return True


def recv_async(channel, marionette_state, input_args):
    recv(channel, marionette_state, input_args, blocking=False)
    return True

#client
#send the stuff n encode, crypt
def send(channel, marionette_state, input_args, blocking=True):
    retval = False

    regex = input_args[0]
    msg_len = int(input_args[1])

    stream_id = marionette_state.get_global(
        "multiplexer_outgoing").has_data_for_any_stream()
    if stream_id or blocking:

        fteObj = marionette_state.get_fte_obj(regex, msg_len)

        bits_in_buffer = len(
            marionette_state.get_global("multiplexer_outgoing").peek(stream_id)) * 8
        min_cell_len_in_bytes = int(math.floor(fteObj.getCapacity() / 8.0)) \
            - fte.encoder.DfaEncoderObject._COVERTEXT_HEADER_LEN_CIPHERTTEXT \
            - fte.encrypter.Encrypter._CTXT_EXPANSION
        min_cell_len_in_bits = min_cell_len_in_bytes * 8

        cell_headers_in_bits = marionette_tg.record_layer.PAYLOAD_HEADER_SIZE_IN_BITS
        cell_len_in_bits = max(min_cell_len_in_bits, bits_in_buffer)
        cell_len_in_bits = min(cell_len_in_bits + cell_headers_in_bits,
                               MAX_CELL_LENGTH_IN_BITS)

        cell = marionette_state.get_global("multiplexer_outgoing").pop(
            marionette_state.get_local("model_uuid"),
            marionette_state.get_local("model_instance_id"),
            cell_len_in_bits)
        ptxt = cell.to_string()
        #changed from 
        #ptxt = str(ptxt)
        #ptxt = scrypt.encrypt(ptxt, password, maxtime=0.1)
        #ptxt = str(ptxt)    
        ptxt = fteObj.encode(ptxt)
        
        #
        #ptxt = str(ptxt)
        ptxt = b64encode(ptxt) 
        #ptxt = str(ptxt)
        #ptxt = str(ptxt)
        #ptxt = gpg.encrypt(ptxt, serverkey)
        ptxt = scrypt.encrypt(ptxt, password, maxtime=0.1)
        #ptxt = str(ptxt)
        #ptxt = gpg.encrypt(ptxt, serverkey)
        #ptxt = str(ptxt)
        ptxt = b64encode(ptxt) 

        #ptxt = str(ptxt)
        ctxt = fteObj.encode(ptxt)
        #to
        ctxt_len = len(ctxt)
        bytes_sent = channel.sendall(ctxt)
        retval = (ctxt_len == bytes_sent)

    return retval

#remove the encr and send it the sock
def recv(channel, marionette_state, input_args, blocking=True):
    retval = False
    regex = input_args[0]
    msg_len = int(input_args[1])

    fteObj = marionette_state.get_fte_obj(regex, msg_len)

    try:
        ctxt = channel.recv()
        if len(ctxt) > 0:
            #start
            #ctxt = fteObj.decode(ctxt)#decode the first layer
            ctxt = str(ctxt)
            ctxt = fteObj.decode(ctxt)
            ctxt = str(ctxt)
            ctxt = b64decode(ctxt)
            ctxt = str(ctxt)
                
            ctxt = scrypt.decrypt(ctxt, password, maxtime=0.1)#then remove scrypt
            ##ctxt = str(ctxt)
            #ctxt = str(ctxt)
            
            #ctxt = gpg.decrypt(ctxt, passphrase=clientpassword)
            #ctxt = str(ctxt)
            
            ctxt = b64decode(ctxt)
            ##ctxt = str(ctxt)
            #stop
            [ptxt, remainder] = fteObj.decode(ctxt)#fteObj.decode(ctxt)
            
            cell_obj = marionette_tg.record_layer.unserialize(ptxt)
            assert cell_obj.get_model_uuid() == marionette_state.get_local(
                "model_uuid")

            marionette_state.set_local(
                "model_instance_id", cell_obj.get_model_instance_id())

            if marionette_state.get_local("model_instance_id"):
                if cell_obj.get_stream_id() > 0:
                    marionette_state.get_global(
                        "multiplexer_incoming").push(ptxt)
                retval = True
    except fte.encrypter.RecoverableDecryptionError as e:
        retval = False
    except Exception as e:
        if len(ctxt)>0:
            channel.rollback()
        raise e

    if retval:
        if len(remainder) > 0:
            channel.rollback(len(remainder))
    else:
        if len(ctxt)>0:
            channel.rollback()

    return retval
