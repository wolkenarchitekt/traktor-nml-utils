from setuptools import setup, find_packages

setup(
    name='traktor-nml-utils',
    version='0.1',
    description='Utilities to read and write Traktor NML files',
    url='http://github.com/ifischer/traktor-nml-utils',
    author='Ingo Fischer',
    author_email='mail@ingofischer.de',
    license='GPL',
    packages=find_packages(exclude=('tests', 'docs')),
    zip_safe=True
)
