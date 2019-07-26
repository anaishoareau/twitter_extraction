# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2019
GitHub : https://github.com/anaishoareau
Linkedin : https://www.linkedin.com/in/ana%C3%AFs-hoareau-a2a042183/
"""
# IMPORT
from setuptools import setup, find_packages

# FONCTION D'INSTALLATION

setup(name='twitter_extraction',
      version='0',
      description='Tweets extraction methods',
      url='https://github.com/anaishoareau/twitter_extraction',
      author='Anaïs HOAREAU',
      packages=find_packages(),
      install_requires=['tweepy','json', 'time', 'sys','date'])
