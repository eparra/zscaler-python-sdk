# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from zscaler_python_sdk import __version__


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

setup(name='zscaler_python_sdk',
      python_requires='>3.8.2',
      version=__version__,
      description='Python Interface to Zscaler API',
      long_description=long_description,
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.8.2',
          'Natural Language :: English',
      ],
      keywords='zscaler python',
      author='Eddie Parra',
      author_email='NO EMAIL',
      maintainer='Eddie Parra',
      maintainer_email='NO EMAIL',
      url='https://github.com/eparra/zscaler-python-sdk/',
      license='MIT',
      packages=['zscaler_python_sdk'],
      install_requires=['requests>=2.25.1'],
      zip_safe=False
)
