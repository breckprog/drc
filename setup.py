import os
import sys

from setuptools import setup, find_packages

py_version = sys.version_info[:2]

PY3 = py_version[0] == 3

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires=[
    'lepton',
    'pyaudio',
    'PyOpenGL',
    ]

tests_require = [
    ]

docs_extras = [
    'Sphinx',
    'docutils',
    'repoze.sphinx.autointerface',
    ]

testing_extras = tests_require + [
    'nose',
    'coverage',
    'virtualenv', # for scaffolding tests
    ]

setup(name='drc',
      version='0.0',
      description=('Audio Visualization'),
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        ],
      keywords='',
      author="Code of Conduct, LLC",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = install_requires,
      extras_require = {
          'testing':testing_extras,
          'docs':docs_extras,
          },
      tests_require = tests_require,
      test_suite="drc.tests",
      entry_points = """\
      """
      )

