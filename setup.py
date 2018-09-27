"""
Devops utils
"""
from setuptools import find_packages, setup

dependencies = ['click']

setup(
    name='devops',
    version='0.1.0',
    url='https://github.com/mabounassif/python-utils-devops',
    license='BSD',
    author='Mahmoud Nassif',
    author_email='mahmoud.abounassif@gmail.com',
    description='Devops utils',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'devops = src.cli:main',
        ],
    }
)
