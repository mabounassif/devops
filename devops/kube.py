from devops.utils import get_template

import click
import subprocess

@click.group()
def kube():
    pass

@kube.command()
def sudo():
    kube_process = subprocess.Popen('kubectl create -f -',
            stdin=subprocess.PIPE,
            shell=True)

    kube_process.communicate(get_template('admin-user-rolebinding').encode())

@kube.command()
def clear():
    kube_process = subprocess.Popen('kubectl delete -f -',
            stdin=subprocess.PIPE,
            shell=True)

    kube_process.communicate(get_template('admin-user-rolebinding').encode())

