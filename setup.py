# coding=utf-8
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'proimp',
]

with codecs.open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='proimp',
    version='0.0.1',
    description='proimp - generates import dependencies',
    long_description=readme,
    author='yan huang',
    author_email='leafyongzhong@gmail.com',
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
