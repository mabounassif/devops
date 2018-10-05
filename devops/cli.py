import click

from devops.helm import helm
from devops.kube import kube

@click.group()
def main():
    pass

main.add_command(helm)
main.add_command(kube)

if __name__ == '__main__':
    main()

