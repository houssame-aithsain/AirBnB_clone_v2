#!/usr/bin/python3
"""
Module to deploy an archive to web servers using Fabric.
"""

import os.path
from fabric.api import *
from fabric.operations import run, put
from datetime import datetime

env.hosts = ['54.84.246.32', '52.91.154.11']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")

    result = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(now))
    if result.failed:
        return None
    else:
        return result


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))

        print('New version deployed!')
        success = True

    except Exception:
        success = False
        print("Could not deploy")
    return success
