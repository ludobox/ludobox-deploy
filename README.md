# Ludobox Deploy

A set of Fabric scripts to deploy Ludobox using Python, Pip, Gunicorn and Supervisor (tested on Debian only).

## Usage

### Define your servers

Copy ```servers.sample.py``` to ```servers.py``` and edit according to your needs

    def prod():
        env.hosts = ['127.0.0.1']
        env.user  = 'ludobox'
        env.remote_admin  = 'junkware'
        env.port="2022"

### Setup the initial environment

    fab prod setup_debian
    fab prod init
    fab prod setup_server # rewrite server config

### Update code and deps

    fab prod deploy

### Remote control your install

    fab prod start
    fab prod restart
    fab prod stop

### Pre-requisites

Install Supervisor and Nginx

    sudo apt-get install supervisor nginx


### TODO

* Prod build with `npm run build` on the `/client` rep
* Auto write Flask config file
* Add provisioning with Chef / Ansible
