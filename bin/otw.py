#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: otw.py

__author__ = 'flipchan/aka\Filip Kälebo'
__version__ = 1.5
#/*
# * ----------------------------------------------------------------------------
# * "THE BEER-WARE LICENSE" (Revision 42):
# * <flipchan@riseup.net> wrote this file. As long as you retain this notice you
# * can do whatever you want with this stuff. If we meet some day, and you think
# * this stuff is worth it, you can buy me a beer in return Filip Kälebo
# * ----------------------------------------------------------------------------
# */
#python off the record crypto with pgp instead of diffie hellman
#inspierd by https://github.com/python-otr/
#build to provide stronger crypto in the LayerProx project

#this is version 1.2 the latest crypto in layerprox
#pgp sign and encrypt -> aes-ctr 256 -> hmac 

from Crypto.Hash import SHA256 as _SHA256
from Crypto.Hash import SHA as _SHA1
from Crypto.Hash import HMAC as _HMAC
from Crypto.Cipher import AES

import gnupg
#gpg = gnupg.GPG(homedir=home)
gpg.encoding = 'utf-8'
fingerprint = ''#fingerprint 
password = ''#gpg passwd
keyide = ''#my key id

#note: i does not know everything about crypto i am no expert on this is, i only do crypto as a hobby 
#i would probelly not recommend implementing this without modifying the code, anyhow this is -->
#my own version of otr(off the record) i call it otw(off the wire), crypto = pgp with sha256hmac160
#in python-otr u only get a 1024 dsa key and i think that is bad so i added pgp support
#import thisfile the run justencrypt() justdecrypt()
#


#change this, its just some test inputs
data = 'test'#test input
key1 = '1234'#hmac key 1
key2 = '4321'#hmac key 2

def SHA256(data):
    return _SHA256.new(data).digest()

def HMAC(key, data, mod):
    return _HMAC.new(key, msg=data, digestmod=mod).digest()

def SHA256HMAC(key, data):
    return HMAC(key, data, _SHA256)

#>>> print len(SHA256HMAC('test', 'test'))
#32



#use sha in aes-ctr?
def SHA256HMAC160(key, data):
    return SHA256HMAC(key, data)[:20]


#only hmac
def genhmac(key, data):
    return SHA256HMAC(key, data)
    
    
    
#>>> secret = os.urandom(16)
#>>> crypto = AES.new(os.urandom(32), AES.MODE_CTR, counter=lambda: secret)
#>>> encrypted = crypto.encrypt("aaaaaaaaaaaaaaaa")    
    

def aesctr_decrypt(key1, key2, data):
    decryptor = AES.new(key1, AES.MODE_CTR, counter=lambda: key2)
    decrypted = decryptor.decrypt(data)    
    return decrypted

def aesctr_crypt(key1, key2, data):
    key1 = SHA256HMAC(key1, data)#32
    if len(key1) == 32 and len(key2) == 16:#32*8 256 
	crypto = AES.new(key1, AES.MODE_CTR, counter=lambda: key2)
	encrypted = crypto.encrypt(data)
	return encrypted	
    else:
	return 'key length is not correct '

    
#sign and encrypt
def justencrypt(key1, key2, data, fingerprint, keyide, password, home):
	#crypt
	thedata = str(data)
	gpg = gnupg.GPG(homedir=home)	
	sig = gpg.sign(thedata, default_key=fingerprint, passphrase=password)
	thedata = gpg.encrypt(sig, fingerprint) #lets just encrypt it to our selfs
	#sha256hmac160
	thedata = aesctr_crypt(key1, key2, thedata) #aes-ctr it
	#thedate = str(thedata) + SHA256HMAC160(key1, key2)#just gen a hmac
	thedata = str(genhmac(key1, key2)) + str(thedata)
	#output
	return thedata

#gpg passwd define
def justdecrypt(key1, key2, data, password, home):
	#decrypt it
	#verify the hmac
	odata = data
	s = data
	gpg = gnupg.GPG(homedir=home)	
	s[:32] = hdata  #pic the first 32chars which should be the hmac
	hdata = str(hdata)
	theh = str(SHA256HMAC160(key1, key2))
	#if the hmac is hmac / verify the hmac
	if theh == hdata:
	    #aes decrypt
		#if the hmac is true verify it 
		s = s[32:] #remove hmac
		#decrypt with aes-ctr
		s = aesctr_decrypt(key1, key2, data)
		s = str(s)
		sig = gpg.decrypt(s, passphrase=password)
		if not sig:
		    return 'test'#   break, return ''
		verify = gpg.verify(sig.data)
		if not verify:
		    print 'nope not verified'
		    return 'no'#break
		return data
	else:#if the hmac is false break *
		return 'error'#break
		
