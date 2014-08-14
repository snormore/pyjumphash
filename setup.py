from distutils.core import setup
setup(
  name = 'jumphash',
  packages = ['jumphash'], # this must be the same as the name above
  version = '0.1',
  description = 'Implementation of the Jump Consistent Hash algorithm in Python. This algorithm performs consistent hashing on integer keys and maps them to integer buckets.',
  author = 'Steven Normore',
  author_email = 'snormore@gmail.com',
  url = 'https://github.com/snormore/pyjumphash',
  download_url = 'https://github.com/snormore/pyjumphash/tarball/0.1',
  keywords = ['jumphash', 'consistent hash', 'hash algorithm', 'hash'],
  classifiers = [],
)
