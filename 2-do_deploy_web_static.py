#!/usr/bin/python3

'''
a script that compresses the web staticc page
'''
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['54.237.102.228', '100.26.166.217']
        env.user = 'ubuntu'
        env.key_filename = '.~/.ssh/id_rsa'

def do_deploy(archive_path):
    '''
    deploys the files to the server web_o1 and web_o2
    '''
    try:
        if not (path.exists(archive_path):
                return False

                #upload an archive
                put(archive_path, '/tmp/')

                # create a target directory
                timestamp = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/releases/web_static_{}/'.format(timestamp))

                #uncompress the archive
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
                        /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                # removes the archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                # move the unzipped to webstatic host
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
                        /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                # removes the extranous web static directory
                run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'\
                        .format(timestamp))

                # deletes the pre existing sym links
                run('sudo rm -rf /data/web_static/current')

                # establishes the symbolic link
                run('sudo ln -s /data/web_static/releases/web_static_{}/ /data/web_static/current'\
                        .format(timestamp))
    except:
        return False
    # for success:
    return True
