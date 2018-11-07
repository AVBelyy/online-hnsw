import os
import sys
import setuptools
from setuptools import setup, Extension
from setuptools.command.install import install
from distutils.command.build import build

__version__ = '1.0.0'

source_files = ['hnsw_wrapper.cpp', 'hnsw_wrapper.i']

ext_modules = [
    Extension(
        '_hnsw_wrapper',
        source_files,
        swig_opts=["-c++", "-extranative"],
        language='c++',
        extra_compile_args=["-std=c++14", "-I../include"],
    ),
]

class CustomBuild(build):
    def run(self):
        self.run_command('build_ext')
        build.run(self)

class CustomInstall(install):
    def run(self):
        self.run_command('build_ext')
        self.do_egg_install()

custom_cmdclass = {'build': CustomBuild, 'install': CustomInstall}

setup(
    name='online_hnsw',
    version=__version__,
    description='HNSW with Online Updates',
    author='A. Belyy, A. Goryachev',
    url='https://github.com/AVBelyy/online-hnsw',
    ext_modules=ext_modules,
    cmdclass=custom_cmdclass,
    install_requires=[],
    setup_requires=[],
    py_modules=['online_hnsw', 'hnsw_wrapper'],
    zip_safe=False,
)
