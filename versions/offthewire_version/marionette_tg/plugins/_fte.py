#!/usr/bin/env python
# coding: utf-8

#maybe use -> AEAD CHACHA20-POLY1303
#pgp sign and verify if the msg if not verify it will break
#New crypto working on
#extra
#https://password-hashing.net/
#https://paragonie.com/white-paper/2015-secure-php-data-encryption
#https://paragonie.com/blog/2015/08/you-wouldnt-base64-a-password-cryptography-decoded
#https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016


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

from otw import justencrypt, justdecrypt

import gnupg
gpg = gnupg.GPG(homedir=home)# gpg home
gpg.encoding = 'utf-8'

#client conf
gpgpassword = clientpassword#client or server password
fingerprint = serverkey#define fingerprint as client or server key

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
    
        ptxt = fteObj.encode(ptxt)


        ptxt = str(ptxt)
        ptxt = b64encode(ptxt)
        ptxt = scrypt.encrypt(ptxt, password, maxtime=0.1)
        ptxt = b64encode(ptxt)

        
        ptxt = str(ptxt)
        ptxt = b64encode(ptxt) 
        ptxt = str(ptxt)
        ptxt = gpg.encrypt(ptxt, fingerprint)
        #and sign it -->
        ptxt = gpg.sign(ptxt)
        #<-
    
        ptxt = str(ptxt)#1
        ptxt = b64encode(ptxt)#1

        ptxt = str(ptxt)
        
        ptxt = b64encode(ptxt)
        ptxt = scrypt.encrypt(ptxt, password, maxtime=0.1)
        ptxt = b64encode(ptxt)
        
        ctxt = fteObj.encode(ptxt) #c goes to p
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
            ctxt = fteObj.decode(ctxt)#decode the first layer
            
            
            ctxt = str(ctxt)
            ctxt = b64decode(ctxt)
            ctxt = scrypt.decrypt(ctxt, password, maxtime=0.1)
            ctxt = b64decode(ctxt)
          
            ctxt = str(ctxt)
            ctxt = b64decode(ctxt)
            ctxt = str(ctxt)
#verify that the data is legit else break -->

            verify = gpg.verify(ctxt)
            if not verify:
                break
            # <--
            ctxt = gpg.decrypt(ctxt, passphrase=gpgpassword)
            
            ctxt = str(ctxt)#1 
            ctxt = b64decode(ctxt)#1
             
            ctxt = str(ctxt)
            
            ctxt = b64decode(ctxt)
            ctxt = scrypt.decrypt(ctxt, password, maxtime=0.1)
            ctxt = b64decode(ctxt)
            
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
