from setuptools import setup, find_packages

setup(
    name         = 'mytestspiders',
    version      = '2.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = testspiders.settings']},
    #scripts = ['bin/testargs.py']
)
