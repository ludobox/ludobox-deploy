#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib import files

from config.servers import staging,  prod

from debian import setup_debian
from server import setup_server, restart
from server import stop_app as stop
from server import start_app as start
from project import setup_project
from content import backup_files, copy_files_locally

def uptime():
    """ Show number of active connections on the server """
    run('uptime')

def remote_info():
    """ Get name and info of remote host """
    run('uname -a')

def local_info():
    """ Get name and info of local host """
    local('uname -a')

def init():
    """ Init setup of the project """
    setup_project()
    setup_server()

def backup():
    backup_files()
    copy_files_locally()

def deploy():
    setup_project()
    restart()
