#problems and fixes

#run -->
apt-get install libgmp-dev libssl-dev libcurl4-openssl-dev libffi-dev python-dev python-cffi
# <--

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
getting a ffi error? apt-get install libffi-dev
getting a setup error(No module named setuptools_ext)?
fix: let this tool upgrade python setuptools https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py


install on raspberrypi:
apt-get install python-dev python-cffi libffi-dev

if you get a pip error try install https://pypi.python.org/pypi/cffi/1.7.0
i got this error:
root@localhost:~/LayerProx/documentation/install# pip
Traceback (most recent call last):
  File "/usr/bin/pip", line 9, in <module>
    load_entry_point('pip==1.5.6', 'console_scripts', 'pip')()
  File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 356, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
  File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 2476, in load_entry_point
    return ep.load()
  File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 2190, in load
    ['__name__'])
  File "/usr/lib/python2.7/dist-packages/pip/__init__.py", line 74, in <module>
    from pip.vcs import git, mercurial, subversion, bazaar  # noqa
  File "/usr/lib/python2.7/dist-packages/pip/vcs/mercurial.py", line 9, in <module>
    from pip.download import path_to_url
  File "/usr/lib/python2.7/dist-packages/pip/download.py", line 22, in <module>
    import requests, six
  File "/usr/lib/python2.7/dist-packages/requests/__init__.py", line 68, in <module>
    _attach_namespace(urllib3, 'requests.packages')
  File "/usr/lib/python2.7/dist-packages/requests/__init__.py", line 63, in _attach_namespace
    module = __import__(name)
  File "/usr/lib/python2.7/dist-packages/urllib3/contrib/pyopenssl.py", line 55, in <module>
    import OpenSSL.SSL
  File "/usr/lib/python2.7/dist-packages/OpenSSL/__init__.py", line 8, in <module>
    from OpenSSL import rand, crypto, SSL
  File "/usr/lib/python2.7/dist-packages/OpenSSL/rand.py", line 11, in <module>
    from OpenSSL._util import (
  File "/usr/lib/python2.7/dist-packages/OpenSSL/_util.py", line 4, in <module>
    binding = Binding()
  File "/usr/lib/python2.7/dist-packages/cryptography/hazmat/bindings/openssl/binding.py", line 89, in __init__
    self._ensure_ffi_initialized()
  File "/usr/lib/python2.7/dist-packages/cryptography/hazmat/bindings/openssl/binding.py", line 113, in _ensure_ffi_initialized
    libraries=libraries,
  File "/usr/lib/python2.7/dist-packages/cryptography/hazmat/bindings/utils.py", line 80, in build_ffi
    extra_link_args=extra_link_args,
  File "/usr/local/lib/python2.7/dist-packages/cffi-1.8.3-py2.7-linux-x86_64.egg/cffi/api.py", line 437, in verify
    lib = self.verifier.load_library()
  File "/usr/local/lib/python2.7/dist-packages/cffi-1.8.3-py2.7-linux-x86_64.egg/cffi/verifier.py", line 114, in load_library
    return self._load_library()
  File "/usr/local/lib/python2.7/dist-packages/cffi-1.8.3-py2.7-linux-x86_64.egg/cffi/verifier.py", line 225, in _load_library
    return self._vengine.load_library()
  File "/usr/local/lib/python2.7/dist-packages/cffi-1.8.3-py2.7-linux-x86_64.egg/cffi/vengine_cpy.py", line 174, in load_library
    lst = list(map(self.ffi._get_cached_btype, lst))
  File "/usr/local/lib/python2.7/dist-packages/cffi-1.8.3-py2.7-linux-x86_64.egg/cffi/api.py", line 409, in _get_cached_btype
    BType = type.get_cached_btype(self, finishlist)
  File "/usr/local/lib/python2.7/dist-packages/cffi-1.8.3-py2.7-linux-x86_64.egg/cffi/model.py", line 61, in get_cached_btype
    BType = self.build_backend_type(ffi, finishlist)
  File "/usr/local/lib/python2.7/dist-packages/cffi-1.8.3-py2.7-linux-x86_64.egg/cffi/model.py", line 507, in build_backend_type
    base_btype = self.build_baseinttype(ffi, finishlist)
  File "/usr/local/lib/python2.7/dist-packages/cffi-1.8.3-py2.7-linux-x86_64.egg/cffi/model.py", line 525, in build_baseinttype
    % self._get_c_name())
cffi.api.CDefError: 'point_conversion_form_t' has no values explicitly defined: refusing to guess which integer type it is meant to be (unsigned/signed, int/long)

