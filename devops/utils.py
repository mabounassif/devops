from devops import env

def get_template(template_name):
    template = env.get_template('%s.j2' % template_name)
    return template.render()

