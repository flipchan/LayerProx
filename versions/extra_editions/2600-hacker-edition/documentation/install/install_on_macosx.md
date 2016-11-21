#How to install on mac osx

you need:
------------
gpg - generate pgp keys
python2.7 - simply install it from python.org
homebrew - (brew) http://brew.sh/

install:
------------
brew install gmp curl
if you get the error "gmp is not linked" run: brew link gmp/sudo brew link gmp
git clone https://github.com/flipchan/LayerProx.git
cd LayerProx && python setup.py install

