this is the 2600 hacker edition of LayerProx this is the edition that i intend to put out live on the net

in this edition:
crypto has been improved
so fte cipher -> scrypt -> pgp -> chacha20_poly1305



# LayerProx
a rebuild of marionette, encrypted proxy that simulates general webtraffic

**Provides strong end to end encryption with scrypt and PGP


Currently works on/with:
-----------------------
Debian 7-8, kali 1-2, mac osx, windows 7
and also works with proxychains so you can proxy applications through it



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
