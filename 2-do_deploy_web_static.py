#!/usr/bin/python3
"""
Module to deploy an archive to web servers using Fabric.
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.84.246.32', '52.91.154.11']



def do_deploy(archive_path):
    """
    Deploy archive!
    Returns False if the file at the path archive_path does't exist
    """

    if !exists(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    rm_extension = "/data/web_static/releases/" + '{}'\
        .format(file_name.split('.'))
    tmp = "/tmp" + file_name

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(rm_extension))
        run("tar -xzf {} -C {}/".format(rm_extension))
        run("rm {}".format(tmp))
        run("mv -rf {}/web_static/* {}/".format(rm_extension, rm_extension))
        run("rm -rf {}/web_static".format(rm_extension))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(rm_extension))

        return True
    except:
        return False
