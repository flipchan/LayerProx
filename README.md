# LayerProx
a rebuild of marionette, encrypted proxy that simulates general webtraffic

Makes Real looking http packages, to avoid censorship why not make the 
data look like social media or something other?

LayerProx takes the orignal data and encrypts it and makes it look like
http. Atm i have implemented ebay,amazon, facebook etc.. plugins to
generate http requests that looks like you are just visiting a popular site
while you are really looking at something else or useing another protocol

Stronger then a vpn, Smarter then a proxy

**Provides strong end to end encryption with scrypt and PGP


Currently works on/with:
-----------------------
Debian 7-8, kali 1-2, mac osx, windows 7, raspberry pi(raspbian jessie)
and also works with proxychains so you can proxy applications through it



Version 1.5:
-----------
version 1.5 will be out soon here is the new features:
connections go like this:
```console
you/user -> Tor -> LayerProx client -> LayerProx server
```
public LayerProx server will come up soon
Securer/more crypto: advance/remove/replace scrypt 


have been added:
stronger pgp code it nows signs and verifies the data and if the 
data is not verified it will break


install:
--------
python setup.py
create a test user on the client and server and then make pgp keys for those two

What is LayerProx?
-----------------
```console
LayerProx is an advanced easy to reprogram proxy
LayerProx operates like this:
you set up a server and client machine you then proxy your 
connection to the client machine useing a socks4a proxy. 
The data then gets encrypted in multiple Layers to 
provide strong end to end encryption. the encryption:

orignal data --> fte cipher --> scrypt --> pgp --> chacha20_poly1305 --> fte cipher + the spoofed http data 

so the data will look like we are just browseing the webb or looking 
at cute cat pictures.
LayerProx is the first project in the world which 
implements "real http spoofing" 
meaning that you can press on the generated http link and 
actually get somewhere 

Why i have added different layers of encryption is to make the 
end to end encryption really strong 
on alot of other applications they have just implemented one crypto
so if the mitm-attacker gets our data he will only need to decrypt one layer
But here i have added multiple layers so the attack will have to work 
him/her self through multiple layers of encryption.

i have(tried) to make it really easy for anyone to modify and rebuild this
so if you feel like changeing the encryption to diffie hellman or something
else it is easy to do so

```

start:
------
```console
./bin/marionette_server --server_ip 0.0.0.0 --proxy_ip 0.0.0.0 --proxy_port 8081 --format custom/ebay --debug

 ./bin/marionette_client --server_ip 0.0.0.0 --client_ip 127.0.0.1 --client_port 8079 --format custom/ebay --debug

./bin/socksserver --local_port 8081


 curl --socks4a 127.0.0.1:8079 example.com
```
0.0.0.0 to bind all interfaces 

**See documenation folder for more documentation and how to guides


LayerProx is a rebuild of https://github.com/marionette-tg/marionette
