#How to install on Windows

install:
python2.7
py2exe
Microsoft Visual C++ Compiler for Python 2.7 http://www.microsoft.com/en-us/download/details.aspx?id=44266
download layerprox as a zip file from github and extract it on your desktop
if you havent installed scrypt and regex2dfa do that
https://pypi.python.org/pypi/scrypt/
https://github.com/kpdyer/regex2dfa

run:
open cmd as administrator(right click on it and run as administrator)
cd in to LayerProx so in my case 
cd C:\Users\yourusername\Desktop\LayerProx-master\
we type "dir" to make sure we are in the right directory
C:\Users\yourusername\Desktop\LayerProx-maser>dir
run python 
C:\Users\yourusername\Desktop\LayerProx-maser>C:\Python27\python.exe setup.py build
C:\Users\yourusername\Desktop\LayerProx-maser>C:\Python27\python.exe setup.py install


if this doesnt work for you can simply use marionette-windows installer
install:
mingw
https://www.vagrantup.com/
https://github.com/marionette-tg/marionette-windows

download the zip file to your desktop
https://github.com/marionette-tg/marionette-windows/archive/master.zip
unzip it
download layerprox and place it in the "build" folder
open a terminal an cd in to that directory and run the command:
vagrant up

