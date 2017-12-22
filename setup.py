# coding: utf-8

import os
import sys
from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name='ecs_manager',
    version='0.0.1',
    url='https://github.com/pistatium/ecs_service_manager',
    author='pistatium',
    description='Manage ecs service',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'boto3',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'ecs_manager=ecs_manager.cmd:main'
        ]
    },
)
