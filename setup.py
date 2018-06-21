# !/usr/bin/env python

from setuptools import setup

setup(
    name="pylooker",
    packages=["pylooker"],
    version="0.3.0",
    description="A Python interface to Looker API",
    author="David Gasquez",
    license="MIT",
    author_email="davidgasquez@gmail.com",
    url="https://github.com/bufferapp/pylooker",
    keywords=["looker"],
    install_requires=["requests"],
)
