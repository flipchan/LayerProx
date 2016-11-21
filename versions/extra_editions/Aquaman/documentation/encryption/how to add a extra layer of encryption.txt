#How to add more encryption


do you want to an extra layer of encryption?
or modify the encryption.


the file you want to change is "plugins/_fte.py"


#encryption
def send(channel, marionette_state, input_args, blocking=True):
    retval = False
        ptxt = cell.to_string()
        ptxt = fteObj.encode(ptxt)
        
        ptxt = b64encode(ptxt) 
        ptxt = scrypt.encrypt(ptxt, password, maxtime=0.1) --> encrypt
        ptxt = b64encode(ptxt) 

        ctxt = fteObj.encode(ptxt)
        #to
        ctxt_len = len(ctxt)
        bytes_sent = channel.sendall(ctxt)
        retval = (ctxt_len == bytes_sent)

i got alot of errors with scrypt but added some base64 and it works good


#decrypt
def recv(channel, marionette_state, input_args, blocking=True):
    retval = False
    regex = input_args[0]
    msg_len = int(input_args[1])

    fteObj = marionette_state.get_fte_obj(regex, msg_len)

    try:
        ctxt = channel.recv()
        if len(ctxt) > 0:
            #start			we start HERE
            #decode the first layer
            ctxt = str(ctxt)
            ctxt = fteObj.decode(ctxt)
            ctxt = str(ctxt)
            ctxt = b64decode(ctxt)
            ctxt = str(ctxt)
                
            ctxt = scrypt.decrypt(ctxt, password, maxtime=0.1)#then remove scrypt
            
            ctxt = b64decode(ctxt)
            [ptxt, remainder] = fteObj.decode(ctxt)#100%decrypted
            
            cell_obj = marionette_tg.record_layer.unserialize(ptxt)
            assert cell_obj.get_model_uuid() == marionette_state.get_local(
  





encrypt:
fte encode
scrypt encrypt
fte encode

decrypt
ftedecode
scrypt decode
fte decode


extra: when i added gpg i needed to string it so base64 and str() can get pretty much
help u get alot of different kinds of crypto working