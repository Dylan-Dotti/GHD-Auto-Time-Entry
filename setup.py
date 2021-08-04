from setuptools import find_packages, setup

# need to run "python setup.py develop" command from the same directory as setup.py
setup(name='app', version='0.1', description='GHD time entry automator',
    install_requires=[], packages=find_packages())