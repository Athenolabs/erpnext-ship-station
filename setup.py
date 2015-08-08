# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='ship_station',
    version=version,
    description='The Ship Station application is to interface with the ShipStation platform',
    author='olhonko',
    author_email='olhonko@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
