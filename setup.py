from setuptools import setup, find_packages

setup(
    name='Gol',
    description='Chronolog command-line tool.',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click==6.7'
    ],
    entry_points='''
        [console_scripts]
        gol=gol.cli:gol
    '''
)
