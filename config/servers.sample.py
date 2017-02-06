from fabric.api import *

def staging():
    env.hosts = ['127.0.0.1']
    env.user  = 'ludobox'
    env.remote_admin  = 'ludobox'
    env.port="2022"

def rpi():
    env.hosts = ['192.168.1.30']
    env.user  = 'pi'
    env.remote_admin  = 'pi'
    env.port="2022"


def prod():
    env.hosts = ['127.0.0.1']
    env.user  = 'ludobox'
    env.remote_admin  = 'junkware'
    env.port="2022"
