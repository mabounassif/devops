from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('devops', 'config-templates'))
