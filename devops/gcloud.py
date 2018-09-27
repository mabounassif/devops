from devops.utils import get_abs_template

import click
import subprocess

@click.group()
def gcloud():
    pass

@gcloud.command()
def sudo():
    subprocess.check_output(
            'kubectl create -f ' + get_abs_template('gcloud-user-rolebinding.yml'),
            stderr=subprocess.STDOUT,
            shell=True)
    click.echo('Set admin privileges')

@gcloud.command()
def clear():
    subprocess.check_output(
            'kubectl delete -f ' + get_abs_template('gcloud-user-rolebinding.yml'),
            stderr=subprocess.STDOUT,
            shell=True)
    click.echo('Clear admin privileges')


