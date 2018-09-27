import os

dir_name = os.path.abspath(os.path.realpath(__file__))

def get_abs_template(template_path):
    return os.path.abspath(os.path.join(dir_name, '../templates', template_path))
