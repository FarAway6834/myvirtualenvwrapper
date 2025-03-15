from setuptools import setup, find_packages
from os import name as __os__

setup(
    name='myvirtualenvwrapper',
    version='0.0.1',
    description='myvirtualenvwrapper install virtualenvwrapper in posix, virtualenvwrapper-win as win',
    author='du7ec',
    author_email='dutec6834@gmail.com',
    url='https://github.com/FarAway6834/myvirtualenvwrapper',
    packages=find_packages(exclude=[]),
    install_requires=[{'posix':'virtualenvwrapper','nt':'virtualenvwrapper-win'}[__os__]],
    keywords=['myvirtualenvwrapper', 'virtualenvwrapper'],
    python_requires='>=2.3',
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
)