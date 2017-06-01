#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import run, cd
from config.settings import CODE_DIR, HOME_DIR

def backup_files():
    """Run backup script to create an archive of content"""
    with cd(CODE_DIR):
        run("./bin/backup")
