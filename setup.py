# coding=utf-8

from setuptools import setup, find_packages

setup(name="route53dyn",
      version="0.1.0",
      options={},
      description="Updates one or more AWS Route53 DNS records",
      author="carlba",
      packages=find_packages(),
      install_requires=['click'],
      entry_points={
          'console_scripts': [
              'route53dyn = route53dyn.cli:main'
          ]
      }
      )
