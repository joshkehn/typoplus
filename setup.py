# coding=utf-8

from __future__ import unicode_literals
from setuptools import setup

VERSION = "0.0.1"

setup(
    name="TypoPlus",
    version=VERSION,
    keywords="markdown text typography",
    description="Enhanced typography for Python-Markdown",
    author="Joshua Kehn",
    author_email="josh@kehn.us",
    install_requires = [
       "Markdown>=2.0"
    ]
)