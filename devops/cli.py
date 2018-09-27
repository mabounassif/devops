import click

from devops.helm import helm
from devops.gcloud import gcloud

@click.group()
def main():
    pass

main.add_command(helm)
main.add_command(gcloud)

if __name__ == '__main__':
    main()

