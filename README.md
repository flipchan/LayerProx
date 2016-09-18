# LayerProx
a rebuild of marionette, encrypted proxy that simulates general webtraffic

Makes Real looking http packages

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
