from setuptools import setup, find_packages

setup(
    name='pokemon',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description='pokemon api'
)
