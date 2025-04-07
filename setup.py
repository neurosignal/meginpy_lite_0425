#!/usr/bin/env python3
from setuptools import setup, find_packages
import codecs

def main():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        
    setup(
            name='meginpy_lite_0425',
            description='To convert the string type digitization into extra type headshape points.',
            long_description = codecs.open('README.rst', encoding='utf8').read(),
            version='0.23.2.2',
            license='BSD-3',
            url='https://github.com/neurosignal/meginpy (in progress)',
            author='Amit Jaiswal',
            author_email = 'amit.jaiswal@megin.fi',
            maintainer='Amit Jaiswal',
            maintainer_email='amit.jaiswal@megin.fi',
            platforms='any',
            classifiers=['Intended Audience :: Science/Research/Clinical research',
                         'Programming Language :: Python',
                         'Topic :: miscs.',
                         'Operating System :: Unix, ?'],
            packages=find_packages(),
            install_requires=['mne', 'paramiko', 'numpy', 'datetime'],
            )

if __name__ == '__main__':
    main()
