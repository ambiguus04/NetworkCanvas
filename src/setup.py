try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'NetworkCanvas'
}

setup(**config)