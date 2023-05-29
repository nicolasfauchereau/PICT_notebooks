from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

import paleopy

setup(name='paleopy',
      description='code for the Past Interpretation of Climate Tool',
      url='https://github.com/nicolasfauchereau/PICT_notebooks',
      author='Nicolas Fauchereau, Andrew Lorrey',
      author_email='Nicolas.Fauchereau@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["tests", "docs"]),
      version=paleopy.__version__,
      zip_safe=False)
