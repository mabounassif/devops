from devops import ENVIRONMENTS 
import click

@click.group()
def helm():
    pass

@helm.command()
@click.argument('stage')
def sudo(stage):
    if stage in ENVIRONMENTS:
        subprocess.check_output(
                'kubectl delete -f ' + get_abs_template('gcloud-user-rolebinding.yml'),
                stderr=subprocess.STDOUT,
                shell=True)
    else:
        click.echo('Available environments', ENVIRONMENTS)

@helm.command()
@click.argument('stage')
def clear(stage):
    if stage in ENVIRONMENTS:
        subprocess.check_output(
                'kubectl delete -f ' + get_abs_template('gcloud-user-rolebinding.yml'),
                stderr=subprocess.STDOUT,
                shell=True)
    else:
        click.echo('Available environments', ENVIRONMENTS)

