from fabric.api import *


def check():
    return run('ls -al /root')

