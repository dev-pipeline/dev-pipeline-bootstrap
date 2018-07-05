#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name="dev-pipeline-bootstrap",
    version="0.2.0",
    package_dir={
        "": "lib"
    },
    packages=find_packages("lib"),

    install_requires=[
        'dev-pipeline-core >= 0.2.0',
        'dev-pipeline-build >= 0.2.0',
        'dev-pipeline-scm >= 0.2.0'
    ],

    entry_points={
        'devpipeline.drivers': [
            'bootstrap = devpipeline_bootstrap.bootstrap:main'
        ]
    },

    author="Stephen Newell",
    description="build tooling for dev-pipeline",
    license="BSD-2"
)
