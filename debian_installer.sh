echo '''
Debian installer
'''
echo 'installing packages'
apt-get install git libgmp-dev python-pip python-dev curl libcurl4-openssl-dev libssl-dev libpth-dev libffi-dev python-cffi libsodium-dev

echo 'update'

apt-get update && apt-get upgrade

echo 'python setup'
pip install fte regex2dfa scrypt
python setup.py build
python setup.py install
echo 'now you just have to configure it :)'

