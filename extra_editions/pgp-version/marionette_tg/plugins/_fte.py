#!/usr/bin/env python
# coding: utf-8

#pgp version of layerprox coded by ~flipchan

from base64 import b64encode, b64decode
import sys, os
import marionette_tg.conf
home = marionette_tg.conf.get("crypt.gpgdir")

#typeofburk = marionette_tg.conf.get("typeofmachine")
#try:
if typeofburk == "server":
    serverpassword = marionette_tg.conf.get("crypt.serverpassword")
    password = marionette_tg.conf.get("serverpgppassword")
    fingerprint = marionette_tg.conf.get("serverkey")
elif typeofburk == "client":
		clientpassword = marionette_tg.conf.get("crypt.clientpassword")
		password = marionette_tg.conf.get("clientpgppassword")
		fingerprint = marionette_tg.conf.get("clientkey")
		pass
	else:
		return 'undefined type of machine, ur options are client or server'



import gnupg
gpg = gnupg.GPG(homedir=home)# gpg home
gpg.encoding = 'utf-8'

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
 
        ptxt = str(ptxt)
        ptxt = b64encode(ptxt) 
        ptxt = str(ptxt)
        
        #and sign it -->
        ptxt = gpg.sign(ptxt, default_key=fingerprint, passphrase=password)
	
	ptxt = gpg.encrypt(ptxt, fingerprint)
    #<- n crypt it
	

        ptxt = str(ptxt)#1
        ptxt = b64encode(ptxt)#1

        ptxt = str(ptxt)
                
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
          
            ctxt = str(ctxt)
            ctxt = b64decode(ctxt)
            ctxt = str(ctxt)
	    ctxt = gpg.decrypt(ctxt, passphrase=gpgpassword)

	    
	    #verify that the data is legit else break -->
            verify = gpg.verify(ctxt)
            if not verify:
                break
            # <--

            ctxt = str(ctxt)#1 
            ctxt = b64decode(ctxt)#1
             
            ctxt = str(ctxt)
            
            
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
