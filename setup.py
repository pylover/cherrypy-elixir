# -*- coding: utf-8 -*-
import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__),'CherrypyElixir', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'",re.S).match(v_file.read()).group(1)

setup(
    name="CherrypyElixir",
    version=package_version,
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="http://packages.python.org/cherrypyelixir",
    description="Elixir plugin for cherrypy",
    maintainer="Vahid Mardani",
    maintainer_email="vahid.mardani@gmail.com",
    packages=["CherrypyElixir"],
    platforms=["any"],
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.txt')).read() ,
    install_requires=['sqlalchemy>=0.7.0, <0.7.9','elixir>=0.7.0, <0.7.9'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: Freeware",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries'
        ],
    )