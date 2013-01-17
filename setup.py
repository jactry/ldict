#!/usr/bin/env python

import os
import py_compile

py_compile.compile("src/ldict.py")
py_compile.compile("src/en_engine.py")
if os.path.exists("/opt/ldict") != True:
    os.system("sudo mkdir /opt/ldict/")
os.system("sudo cp -a src/* /opt/ldict/")
os.system("sudo cp ldict /usr/bin/")
home = os.getenv("HOME")
os.system("mkdir -p " + home + "/.ldict/dict/")
os.system("mkdir -p " + home + "/.ldict/audio/")
