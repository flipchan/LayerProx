echo 'u need to run this as root'

echo 'installing packages'
apt-get install python2.7 libgmp-dev python-pip python-dev libcurl4-openssl-dev libssl-dev libpth-dev python-cffi libffi-dev 
pip install fte regex2dfa gnupg flask
echo 'i recommend setting up a testuser with gnupg so the homedir = /home/testuser/.gnupg'
apt-get update && apt-get upgrade
echo 'more packages'
cd documentation/install && tar -xvf cffi-1.7.0.tar.gz && cd cffi-1.7.0/  && python setup.py build && python setup.py install
cd ../../../
echo "installing leveldb"
apt-get install libleveldb-dev
pip install plyvel
echo 'configure it'
vim marionette_tg/marionette.conf

python setup.py build
python setup.py install
echo 'createing symlink with conf file'
ln -s /usr/local/lib/python2.7/dist-packages/marionette_tg-0.0.3-py2.7.egg/marionette_tg/marionette.conf  marionette_tg/marionette.conf 
echo 'done'
