#To setup our project as a local package.

from setuptools import find_packages, setup

setup(
    name = 'Generative AI Project-1', #package name
    version= '0.0.0',
    author= 'Charan',
    author_email= 'mcharan1996@gmail.com',
    packages= find_packages(), #find_packages will find __init__.py and considers src as local package.
    install_requires = []

)