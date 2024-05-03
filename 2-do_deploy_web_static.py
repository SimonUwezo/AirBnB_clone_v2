#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
import sys

env.hosts = ['54.157.171.216', '35.174.213.220']


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        print("Error: Archive file does not exist.")
        return False

    try:
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        remote_path = "/data/web_static/releases/"

        # Upload archive
        put(archive_path, '/tmp/')

        # Create directory
        run('mkdir -p {}{}/'.format(remote_path, folder_name))

        # Extract archive
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, remote_path, folder_name))

        # Delete archive
        run('rm /tmp/{}'.format(file_name))

        # Move files
        run('mv {0}{1}/web_static/* {0}{1}/'.format(remote_path, folder_name))

        # Remove extracted folder
        run('rm -rf {}{}/web_static'.format(remote_path, folder_name))

        # Update symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(remote_path, folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Error: {}".format(e))
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: fab -f <fabfile> do_deploy:archive_path=<archive_path>")
        sys.exit(1)

    archive_path = sys.argv[1].split('=')[-1]
    do_deploy(archive_path)
