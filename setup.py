from setuptools import setup

setup(
    name='reddit_lib',
    version='0.1.0',
    packages=['reddit_parser', 'reddit_parser.classes', 'reddit_parser.parsers'],
    author='temkuz',
    author_email='temkuz@bk.ru',
    description='Python library for parsing reddit without using api',
    requires=['requests>=2.28.1']
)