from setuptools import setup, find_packages

setup(
    name='reddit_lib',
    version='0.1.0',
    packages=find_packages(),
    author='temkuz',
    author_email='temkuz@bk.ru',
    description='Python library for parsing reddit without using api',
    install_requires=['requests']
)