"""Setup file for enigma package"""
from setuptools import setup, find_packages

setup(
    name="enigma",
    version="1.0",
    description="Enigma Encryption Machine",
    author="Timothy May",
    author_email="tmay7867@gmail.com",
    keywords="enigma encryption machine",
    packages=find_packages(),
    install_requires=["pandas"]
)
