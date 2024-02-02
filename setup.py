from setuptools import setup

from src import __version__

setup(
    name='liquid_s4',
    version=__version__,

    url='https://github.com/smitkalathiya/liquid-s4.git',
    author='Smit K',
    author_email='smit.patel1436@gmail.com',

    py_modules=['src'],
)