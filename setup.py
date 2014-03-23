import sys
from setuptools import setup, find_packages

py26_dependency = []
if sys.version_info <= (2, 6):
    py26_dependency = ["argparse >= 1.2.1"]

setup(
    name='nbtemplate',
    version='0.0.0',
    description="Render iPython notebooks to other layouts, via templates. Library and command-line tool.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3'
    ],
    keywords='ipython notebooks nbconvert',
    author='Jeremy Singer-Vine',
    author_email='jsvine@gmail.com',
    url='http://github.com/jsvine/nbtemplate/',
    license='MIT',
    packages=find_packages(exclude=['test',]),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        "ipython >= 1.0.0"
    ] + py26_dependency,
    extras_require={
        "markdown": [ "markdown" ]    
    },
    tests_require=[],
    test_suite='test',
    entry_points={
        'console_scripts': [
            'nbtemplate = nbtemplate.cli:main',
        ]
    }
)
