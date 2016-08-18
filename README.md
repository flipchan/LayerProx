# LayerProx
a rebuild of marionette, encrypted proxy that simulates general webtraffic

install:
python setup.py
create a test user on the client and server and then make pgp keys for those two

start:
./bin/marionette_server --server_ip 0.0.0.0 --proxy_ip 0.0.0.0 --proxy_port 8081 --format custom/ebay --debug

 ./bin/marionette_client --server_ip 0.0.0.0 --client_ip 127.0.0.1 --client_port 8079 --format custom/ebay --debug

./bin/socksserver --local_port 8081


 curl --socks4a 127.0.0.1:8079 example.com
0.0.0.0 to bind all interfaces 

Full documentation and extra parts of code will come soon, this is the first part to get the code and whitepaper out there