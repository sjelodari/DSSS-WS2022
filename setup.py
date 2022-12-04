from distutils.core import setup
from setuptools import find_packages

setup(
    name="snowflake",
    version="0.1",
    author="Saber",
    author_email="saber.jelodari@fau.de",
    pakages=find_packages(),
    install_requires=["numpy","turtles","random"],
)