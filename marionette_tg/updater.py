import os
import sys
import tarfile
import tempfile
import threading

from twisted.internet import threads
from twisted.internet import defer

import pycurl

sys.path.append('.')

import marionette_tg.conf
import marionette_tg.dsl

class Downloader(threading.Thread):

    def __init__(self, src_url, dst_path,
                 socks_ip=None, socks_port=None):
        super(Downloader, self).__init__()
        self.src_url_ = src_url
        self.dst_path_ = dst_path
        self.socks_ip_ = socks_ip
        self.socks_port_ = socks_port

    def run(self):
        with open(self.dst_path_, 'w+b') as fh:
            c = pycurl.Curl()
            c.setopt(pycurl.URL, self.src_url_)
            c.setopt(c.WRITEDATA, fh)
            if self.socks_ip_ and self.socks_port_:
                c.setopt(pycurl.PROXY, self.socks_ip_)
                c.setopt(pycurl.PROXYPORT, self.socks_port_)
                c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS4)
            c.perform()

        return self.dst_path_

def download_wrapper(use_marionette, url, dst_path, format_package):
    socks_ip = None
    socks_port = None
    if use_marionette:
        socks_ip = marionette_tg.conf.get("client.client_ip")
        socks_port = marionette_tg.conf.get("client.client_port")

    downloader = Downloader(url, dst_path, socks_ip, socks_port)
    downloader.run()

    return (format_package, dst_path)

class FormatUpdater(object):

    def __init__(self, addr, use_marionette=True, callback=None):
        self.addr_ = addr
        self.use_marionette_ = use_marionette
        self.callback_ = callback

    def do_update(self):
        manifest_file_url = 'http://%s/manifest.txt' % (self.addr_)

        fh = tempfile.NamedTemporaryFile()
        d = threads.deferToThread(download_wrapper, self.use_marionette_,
                                  manifest_file_url, fh.name,
                                  None)
        d.addCallback(self.unpack_manifest)

    def unpack_manifest(self, result):
        (format_package, manifest_path) = result

        with open(manifest_path) as f:
            manifest_contents = f.read()

        format_packages = manifest_contents.strip().split('\n')
        while '' in format_packages: format_packages.remove('')

        for format_package in format_packages:
            if not self.package_exists(format_package):
                self.install_package(format_package)

    def package_exists(self, format_package):
        format_dir = marionette_tg.dsl.get_format_dir()
        package_dir = os.path.join(format_dir, format_package)
        return os.path.isdir(package_dir)

    def install_package(self, format_package):
        package_file_url = 'http://%s/%s.tar.gz' % (self.addr_, format_package)

        fh = tempfile.NamedTemporaryFile()
        d = threads.deferToThread(download_wrapper, self.use_marionette_,
                                  package_file_url, fh.name,
                                  format_package)
        d.addCallback(self.extract_package)

    def extract_package(self, result):
        (format_package, package_path) = result

        format_dir = marionette_tg.dsl.get_format_dir()
        package_dir = os.path.join(format_dir, format_package)

        tar = tarfile.open(package_path, "r:gz")
        tar.extractall(package_dir)
        tar.close()

        if self.callback_:
            self.callback_()
