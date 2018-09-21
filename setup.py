#!/usr/bin/env python
from setuptools import setup, find_packages


def read_file(name):
    with open(name) as f:
        return f.read().strip()


install_requires = [
    'dataclasses',
]

setup(
    name='shrug-lang',
    version='0.0.1',
    description='Interpreter for the Shrug Programming Language',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    maintainer='Ben Wu',
    maintainer_email='bwub124@gmail.com',
    url='https://github.com/Ben-Wu/ShrugProgrammingLanguage',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        shruglang=shrug_lang.interpreter:start_interpreter
    """,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 2 - Pre-Alpha',
    ]
)
