from setuptools import setup
from distutils.extension import Extension

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='trialpkg',
    #url='https://github.com/yaesoubilab/StatTest.git',
    #author='Reza Yaesoubi',
    # Needed to actually package something
    packages=['trialpkg'],
    #ext_modules=[Extension("test", ["test.c"])],
    # Needed for dependencies
    #install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='unlicensed',
    #description='Stats package',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
