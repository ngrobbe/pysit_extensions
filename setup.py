from setuptools import setup, find_packages
from distutils.core import Extension
from distutils import sysconfig
import numpy as np
import platform
import os


setup( # Update these.  Replace 'template' with the name of your extension.
    version = '0.0', 
    name = 'pysit_extensions.example',
    description = 'A template for setting up pysit extension packages.',
    
    # Do not change any of these unless you know what you are doing.
    install_requires = ['setuptools'],
    packages=find_packages(),
    namespace_packages = ['pysit_extensions'],
    zip_safe = False
    )
