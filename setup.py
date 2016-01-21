#!/usr/bin/env python

import os
import re
import sys
from pip.req import parse_requirements

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'awvspy',
    'awvspy.packages',
    'awvspy.packages.sqlalchemy_access',
    'awvspy.packages.sqlalchemy_access.sqlalchemy_access'
]

install_reqs = parse_requirements('requirements.txt',session=False)
requires = [str(ir.req) for ir in install_reqs]

version = ''
with open('awvspy/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='awvspy',
    version=version,
    keywords = ('awvs', 'Acunetix Web Vulnerability Scanner'),
    description='AWVS Python Library.',
    long_description=readme + '\n\n' + history,
    author='wcc526',
    author_email='949409306@qq.com',
    url='http://www.python.org',
    packages=packages,
    package_data={'': ['LICENSE'], 'awvspy': ['*.pem']},
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ),
    extras_require={
    },
)
