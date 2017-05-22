#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.contrib import files
from fabvenv import virtualenv, make_virtualenv
from config.settings import *

def setup_project():
    """ Update the last version of the project """
    update_code_from_git()
    create_virtual_env()
    install_python_app()
    update_requirements()
    install_python_app()
    if USE_BOWER : bower_install()

def create_virtual_env():
    """ Create a virtual environment for Python"""
    if not files.exists(VIRTUALENV_PATH):
        make_virtualenv(VIRTUALENV_PATH)

def create_pid_dir():
    """ Create directory to store PID information """
    run("mkdir -p %s"%RUN_DIR)

def update_code_from_git():
    """ Download latest version of the code from git """
    if not files.exists(CODE_DIR):
        run("git clone %s" % MAIN_GITHUB_REP )
    with cd(CODE_DIR):
        run("git pull")

def update_requirements():
    """ Update external dependencies on host """
    with virtualenv(VIRTUALENV_PATH):
        cmd = ['pip install']
        cmd += ['--requirement %s' %  os.path.join(PYTHON_APP_DIR,'requirements.txt')]
        run(' '.join(cmd))

def install_python_app():
    """ Update external dependencies on host """
    with virtualenv(VIRTUALENV_PATH):
        with cd(PYTHON_APP_DIR):
            cmd = "python setup.py develop" # use develop flag to allow new versions
            run(cmd)
