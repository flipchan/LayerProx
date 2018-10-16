# LayerProx
A rebuild of marionette, encrypted proxy that simulates general webtraffic.

# This project is not longer being developed due to real life things, 
## For an updated version follow the great developers over at redjack 
# Here https://github.com/redjack/marionette is the updated maintain program by redjack , i advise all to use that program instead of this one


'''
this is the dev version for other versions visit the folders
ls versions/
ls extraversions/
'''

##Openbsd dev? contact me at -> flipchan[at]riseup.net or layerproxdevelopment[at]tomuchmoney.club
###short update 11/01-2017, i been working on a ring scheme as auth but putting that aside and working on a stable version with off the wire

core idea of LayerProx project make the person that is intercepting our data for example a mitm belive that we are visiting 
site "X" when we are on site "Y"

Makes Real looking http packages, to avoid censorship why not make the 
data look like social media or something other?

LayerProx takes the orignal data and encrypts it and makes it look like
http. At the moment I have implemented ebay, amazon, facebook etc.. plugins to
generate http requests that looks like you are just visiting a popular site
while you are really looking at something else or useing another protocol

Stronger than a vpn, Smarter than a proxy.

LayerProx believes in Privacy so it comes with a Warrant Canary

**Provides strong end to end encryption with PGP + AES-CTR + BLAKE-HMAC**

##Whats is uniq with layerprox?
a normal obfusciation system makes the data look like random http data. 
this projects makes it look like the packages are goin to facebook, ebay etc.
This project makes the packages look like user a visit site b. but user a is really visits site c
By doing this we bypass deep package inspection systems(the data just looks like regular traffic) and the encryption
protects against deep package injection

encryption: pgp + aes-ctr + hmac
			Encrypt then HMAC yesyes
each user has its uniq keys for the crypto with a expire date to help improve security

Currently works on/with:
-----------------------
Debian 7-8, kali 1-2, mac osx, windows 7, raspberry pi(raspbian jessie), ubuntu 16.10
and also works with proxychains so you can proxy applications through it



##i recommend that you wait deploying this until version offthewire is stable (a day or two)

layerprox changes your traffic so it looks like your doing something else 



Version 2:
-----------
version 2  will be out soon here is the new features:
connections go like this:
```console
you/user -> Tor -> LayerProx client -> LayerProx server
```
public LayerProx server will come up soon


have been added:
crypto sys: pgp + aes-ctr + hmac

install:
--------
python setup.py install/build - its recommended that u use a stable version and an installer
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
follow start.txt guide to configure it 

./bin/marionette_server --server_ip 0.0.0.0 --proxy_ip 0.0.0.0 --proxy_port 8081 --format custom/ebay --debug

 ./bin/marionette_client --server_ip 0.0.0.0 --client_ip 127.0.0.1 --client_port 8079 --format custom/ebay --debug

./bin/socksserver --local_port 8081


 curl --socks4a 127.0.0.1:8079 example.com
```
0.0.0.0 to bind all interfaces 

**See documenation folder for more documentation and how to guides**


LayerProx is based on https://github.com/marionette-tg/marionette


i recommend u check out the wiki for more info
