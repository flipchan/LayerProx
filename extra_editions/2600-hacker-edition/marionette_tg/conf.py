#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import ConfigParser

def find_conf_file():
    search_dirs = ['.',
                   sys.prefix,
                   '/etc',
                   os.path.dirname(__file__),
                  ]
    for dir in search_dirs:
        conf_path = os.path.join(dir, 'marionette.conf')
        if os.path.exists(conf_path):
            return conf_path
        conf_path = os.path.join(dir, 'marionette_tg', 'marionette.conf')
        if os.path.exists(conf_path):
            return conf_path

    return None

def parse_conf():
    global conf_

    confparser = ConfigParser.SafeConfigParser()
    conf_file_path = find_conf_file()
    if not conf_file_path:
        raise Exception('can\'t find marionette_tg.conf')
    confparser.read(conf_file_path)

    conf_ = {}
    try:
        conf_["general.debug"] = confparser.getboolean("general", "debug")
        conf_["general.autoupdate"] = confparser.getboolean("general",
            "autoupdate")
        conf_["general.update_server"] = confparser.get("general",
            "update_server")
        conf_["general.format"] = confparser.get("general", "format")
        conf_["client.client_ip"] = confparser.get("client", "client_ip")
        conf_["client.client_port"] = confparser.getint(
            "client", "client_port")
	conf_["crypt.scrypt"] = confparser.get('crypt', 'scrypt')
	#conf_["crypt.serverkey"] = confparser.get("crypt", "serverkey")
	conf_["crypt.clientkey"] = confparser.get('crypt', 'clientkey')
	conf_["crypt.serverkey"] = confparser.get('crypt', 'serverkey')
 	conf_["crypt.serverhomedir"] = confparser.get('crypt', 'serverhomedir')
	conf_["crypt.clientpassword"] = confparser.get('crypt', 'clientpassword')
	conf_["crypt.serverpassword"] = confparser.get('crypt', 'serverpassword')
	conf_["crypt.clienthomedir"] = confparser.get('crypt', 'clienthomedir')
        conf_["server.server_ip"] = confparser.get("server", "server_ip")
        conf_["server.proxy_ip"] = confparser.get("server", "proxy_ip")
        conf_["server.proxy_port"] = confparser.getint("server", "proxy_port")
    except:
        print 'cannot parse conf file'
        sys.exit(1)


def get(key):
    global conf_

    try:
        retval = conf_[key]
    except:
        parse_conf()
    finally:
        retval = conf_[key]

    return retval

def set(key, value):
    global conf_

    try:
        conf_[key] = value
    except:
        parse_conf()
    finally:
        conf_[key] = value
