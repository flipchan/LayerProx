#problems and fixes



Problems and fixes:
cant connect remotely to it?
i solved this by switching from 127.0.0.1 to 0.0.0.0 mainly because 127.0.0.1 = localhost
and 0.0.0.0 binds all interfaces

cant install pycurl?
could not run  curl-config
#include <openssl/crypto.h> error 
apt-get install libcurl4-openssl-dev
apt-get install libssl-dev

if u need to cffi upgrade
pip install cffi==1.7.0

cant install regex2dfa?
getting a ffi error? apt-get install libffi
getting a setup error(No module named setuptools_ext)?
fix: let this tool upgrade python setuptools https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py


