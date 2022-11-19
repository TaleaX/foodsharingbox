#!/usr/bin/env python

import paramiko
from scp import SCPClient

def transfer():
    credentials = []
    
    with open(".env", "r") as env:
        for line in env:
            credentials.append(line.strip())

    def createSSHClient(server, port, user, password):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, port, user, password)
        return client

    ssh = createSSHClient(credentials[0], credentials[1], credentials[2], credentials[3])

    with SCPClient(ssh.get_transport()) as scp:
        scp.put('static/image.jpg', '/srv/foodsharingbox/image.jpg')