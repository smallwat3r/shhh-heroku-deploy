"""This file is used to acquire the Shhh source code."""

import shutil
import urllib.request

from setuptools import setup

url = "https://github.com/smallwat3r/shhh/archive/refs/heads/master.zip"
file_name = 'shhh.zip'

# download latest Shhh source code
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

# unpack the zip archive
shutil.unpack_archive(file_name)

# move source code content in current directory
shutil.copytree("shhh-master", ".",
                dirs_exist_ok=True,
                ignore=shutil.ignore_patterns("*.toml", "*.yml", "*.md"))

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setup(name="shhh", install_requires=install_requires)
