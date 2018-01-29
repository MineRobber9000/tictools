#!/usr/bin/env python

from setuptools import setup

install_requires = []

setup(
    name='tictools',
    version='0.1.0',
    description='A tool for generating TIC-80 carts',
    long_description='A tool for generating TIC-80 carts.',
    author='Robert Miles',
    author_email='milesrobert374@gmail.com',
    url='https://github.com/MineRobber9000/tictools',
    keywords='toolset',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=['tictools'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'codesize=tictools.console:codesize',
        ],
    }
)
