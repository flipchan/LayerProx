                                                                                   .         .                                                  
         .8.           ,o888888o.     8 8888      88        .8.                   ,8.       ,8.                   .8.          b.             8 
        .888.       . 8888     `88.   8 8888      88       .888.                 ,888.     ,888.                 .888.         888o.          8 
       :88888.     ,8 8888       `8b  8 8888      88      :88888.               .`8888.   .`8888.               :88888.        Y88888o.       8 
      . `88888.    88 8888        `8b 8 8888      88     . `88888.             ,8.`8888. ,8.`8888.             . `88888.       .`Y888888o.    8 
     .8. `88888.   88 8888         88 8 8888      88    .8. `88888.           ,8'8.`8888,8^8.`8888.           .8. `88888.      8o. `Y888888o. 8 
    .8`8. `88888.  88 8888     `8. 88 8 8888      88   .8`8. `88888.         ,8' `8.`8888' `8.`8888.         .8`8. `88888.     8`Y8o. `Y88888o8 
   .8' `8. `88888. 88 8888      `8,8P 8 8888      88  .8' `8. `88888.       ,8'   `8.`88'   `8.`8888.       .8' `8. `88888.    8   `Y8o. `Y8888 
  .8'   `8. `88888.`8 8888       ;8P  ` 8888     ,8P .8'   `8. `88888.     ,8'     `8.`'     `8.`8888.     .8'   `8. `88888.   8      `Y8o. `Y8 
 .888888888. `88888.` 8888     ,88'8.   8888   ,d8P .888888888. `88888.   ,8'       `8        `8.`8888.   .888888888. `88888.  8         `Y8o.` 
.8'       `8. `88888.  `8888888P'  `8.   `Y88888P' .8'       `8. `88888. ,8'         `         `8.`8888. .8'       `8. `88888. 8            `Yo 
					AQUAMAN EDITION - released at SEC-T 0x09 



#Aquaman
in this edition i have replaces the python twister logging with the string fish and some "randomly" generated characters









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
