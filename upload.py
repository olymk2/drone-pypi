#!/usr/bin/python
import os
import sys
import subprocess


PYPI_USERNAME = os.environ.get('PYPI_USERNAME')
PYPI_PASSWORD = os.environ.get('PYPI_PASSWORD')
PYPI_REPOSITORY = os.environ.get(
    'PYPI_REPOSITORY',
    'https://test.pypi.org/legacy/')


# sanity checks
if PYPI_USERNAME is None:
    sys.exit('No username supplied set PYPI_USERNAME')
if PYPI_PASSWORD is None:
    sys.exit('No password supplied set PYPI_PASSWORD')
print('DRONE_PYPI uploading to %s' % PYPI_REPOSITORY)

# write out the .pyirc file with credentials
with open('/root/.pypirc', 'w') as fp:
    fp.write("""
[distutils]
index-servers=
    pypi

[pypi]
repository:{url}
username:{username}
password:{password}
    """.format(**{
        'username': PYPI_USERNAME,
        'password': PYPI_PASSWORD,
        'url': PYPI_REPOSITORY
    }))

# run the actual pypi upload
subprocess.call(['python', 'setup.py', 'sdist', 'upload', '-rpypi'])
