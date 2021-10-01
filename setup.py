# *-* coding:utf-8 *-*

import setuptools

with open('README.md', 'r') as f:
  long_description = f.read()

with open('requirements.txt', 'r') as f:
  required = f.read().splitlines()

setuptools.setup(
  name='tago',
  version='3.0.11',
  python_requires='>=3.6',
  description='Official Python lib for TagoIO',
  long_description=long_description,
  long_description_content_type="text/markdown",
  classifiers=[
      'Development Status :: 5 - Production/Stable',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python :: 3 :: Only',
      'Topic :: Software Development :: Libraries :: Python Modules',
  ],
  keywords='tago tagoio develop iot sdk analysis device',
  url='https://github.com/tago-io/tago-sdk-python',
  author='Tago LLC',
  author_email='dev@tago.io',
  license='Apache License',
  packages=setuptools.find_packages(),
  install_requires=required,
  zip_safe=False
)
