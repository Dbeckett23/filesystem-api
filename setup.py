"""
Insta485 python package configuration.
Andrew DeOrio <awdeorio@umich.edu>
"""

from setuptools import setup

setup(
    name='filesystem',
    version='0.1.0',
    packages=['filesystem'],
    include_package_data=True,
    install_requires=[
        'Flask==1.1.1',
        'html5validator==0.3.3',
        'pytest==5.3.5',
        'pytest-flask==0.15.1',
    ],
)