#!/usr/bin/python3
"""
A fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo.
"""

from os import path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    A function that generates an archive
    """
    date = datetime.now()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day,
        date.hour, date.minute, date.second
    )
    if not path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    cmd = "cd web_static && tar -cvzf ../{} . && cd -".format(archive)
    if local(cmd).succeeded:
        return archive
    return None
