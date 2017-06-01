#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
from fabric.api import run, cd, local, env
from config.settings import CODE_DIR, HOME_DIR

def backup_files():
    """Run backup script to create an archive of content"""
    with cd(CODE_DIR):
        run("./bin/backup")

def copy_files_locally():
    backup_path = os.path.join(CODE_DIR,"backups")

    # local_backup_dir
    local_backup_dir = os.path.join(os.getcwd(), 'backups')
    if not os.path.exists(local_backup_dir):
        os.makedirs(local_backup_dir)

    filename = run("ls -t %s | head -1"%backup_path)
    backup_filename = os.path.join(backup_path,filename)
    
    local_backup_filename = os.path.join(local_backup_dir,filename)

    local('scp %s@%s:%s %s'%(env.user,env.host,backup_filename,local_backup_filename))
