__author__ = 'Robert P. Cope'
__author_email__ = 'rpcope1@gmail.com'
__app_name__ = 'Hacker News Atom Feed Generator'
__version__ = '0.1.0'


from setuptools import setup

setup(name=__app_name__,
      author=__author__,
      author_email=__author_email__,
      version=__version__,
      scripts=['HNAtomFeedServe.py'],
      install_requires=['pyatom', 'HackerNewsAPI'])
