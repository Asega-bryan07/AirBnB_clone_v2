#!/usr/bin/python3

import os
from fabric.api import *

env.hosts = ['54.237.102.228','100.26.166.217']

def do_clean(number=0):
    '''
    deletes an archive that is out of date
    '''

    number = 1 if int(number) == else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop()] for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
