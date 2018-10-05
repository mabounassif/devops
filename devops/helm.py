from devops.utils import get_template

import click
import subprocess

@click.group()
def helm():
    pass

@helm.command()
@click.argument('stage')
def sudo(stage):
    subprocess.check_output(
            'kubectl create -f - %s' % get_template('kube-user-rolebinding'),
            stderr=subprocess.STDOUT,
            shell=True)

@helm.command()
@click.argument('stage')
def clear(stage):
    subprocess.check_output(
            'kubectl delete -f - %s' % get_template('kube-user-rolebinding'),
            stderr=subprocess.STDOUT,
            shell=True)

