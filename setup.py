from setuptools import find_packages, setup

# need to run "python setup.py develop" command from the same directory as setup.py
setup(name='app', version='1.0', description='GHD time entry automator',
    install_requires=[], packages=find_packages())