import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='traktor-nml-utils',
    version='2.0.4',
    description='Utilities to read and write Traktor NML files',
    long_description=read('README.pypi.md'),
    long_description_content_type='text/markdown',
    url='http://github.com/ifischer/traktor-nml-utils',
    author='Ingo Fischer',
    author_email='mail@ingofischer.de',
    license='GPL',
    packages=find_packages(exclude=('tests', 'docs')),
    zip_safe=True,
    python_requires='>=3.7.0',
    install_requires=[
        'xsdata',
    ],
)
