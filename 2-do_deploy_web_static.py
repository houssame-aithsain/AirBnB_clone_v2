#!/usr/bin/python3
"""
Module to deploy an archive to web servers using Fabric.
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['xx-web-01', 'xx-web-02']


def do_deploy(archive_path):
    """
    Deploys an archive to web servers.

    Args:
        archive_path (str): The path to the archive to deploy.

    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        dest_dir = "/data/web_static/releases/" + no_ext + "/"
        put(archive_path, "/tmp/" + file_name)
        run("mkdir -p " + dest_dir)
        run("tar -xzf /tmp/" + file_name + " -C " + dest_dir)
        run("rm /tmp/" + file_name)
        run("mv " + dest_dir + "web_static/* " + dest_dir)
        run("rm -rf " + dest_dir + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + dest_dir + " /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
