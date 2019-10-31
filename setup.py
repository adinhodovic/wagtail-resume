#!/usr/bin/env python
import os
import re

from setuptools import find_packages, setup


def get_version(*file_paths):
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


version = get_version("wagtail_resume", "__init__.py")

readme = open("README.md").read()


setup(
    name="wagtail-resume",
    version=version,
    description="""Wagtail resumes for developers""",
    long_description=readme,
    author="Dani Hodovic",
    author_email="hodovic.dani@gmail.com",
    url="https://github.com/danihodovic/wagtail-resume",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'wagtail-markdown@git+https://github.com/danihodovic/wagtail-markdown@bump-dependencies',
        'wagtail>=2',
        'wagtail-metadata>=3',
    ],
    license="MIT",
    keywords="[django,wagtail,resume]",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
