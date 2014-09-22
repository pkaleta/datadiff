from distutils.core import setup
from setuptools import find_packages
import setuptools # for extra commands

exec(open('datadiff/version.py').read())
setup(
    name = 'datadiff',
    packages = find_packages(),
    version = __version__,
    description = 'DataDiff is a library to provide human-readable diffs of python data structures.',
    long_description = __doc__,
    test_suite = "nose.collector",
    author = 'Dave Brondsema',
    author_email = 'dave@brondsema.net',
    url = 'http://sourceforge.net/projects/datadiff/',
    keywords = ['data', 'diff'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license = 'Apache License',
)
