# *-* coding:utf-8 *-*

from setuptools import setup

setup(name='tago',
      version='2.0.0',
      description='Official Python lib for Tago',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: Other/Proprietary License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='tago iot raspberrypi raspberry',
      url='https://github.com/tago-io/tago-python',
      author='Tago LLC',
      author_email='dev@tago.io',
      license='Copyright',
      packages=['tago', 'tago/device'],
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=['socketIO-client', 'requests', 'promise','requests-mock'],
      zip_safe=False)
