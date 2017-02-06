#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import *

MAIN_GITHUB_REP = "https://github.com/ludobox/ludobox.git"
HOME_DIR ="/home/ludobox/"
APP_NAME = "ludobox"

LOG_DIR=os.path.join(HOME_DIR,"log")
CODE_DIR=os.path.join(HOME_DIR, APP_NAME)
MODULE_NAME = "wsgi.py" #
APP_MAIN_FILE = "application"

VIRTUALENV_PATH=os.path.join(HOME_DIR,'venv')
STATIC = os.path.join(CODE_DIR,'app/static')
USE_BOWER = False

WEBPORT=8080

RUN_DIR=os.path.join(HOME_DIR,"run")
USGWI_SOCKET=os.path.join(RUN_DIR,".%s.sock"%APP_NAME)
TOPOGRAM_PID=os.path.join(RUN_DIR,"%s.pid"%APP_NAME)

CONFIG_DIR=os.path.join(HOME_DIR,"config")
UPLOADS_DIR=os.path.join(HOME_DIR,"uploads")
