#!/usr/bin/python3
"""
Module to generate a .tgz archive from the contents of the web_static folder
using the function do_pack.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    The archive is stored in the folder 'versions'.
    Returns the archive path if the archive has been correctly generated,
    otherwise returns None.
    """
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(date_time)
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        return None
