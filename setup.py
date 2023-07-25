'''
Created on Feb 16, 2017
'''

from setuptools import setup

from cafy_pytest.__version__ import __version__

setup(
    name="cafy_pytest",
    packages=['cafy_pytest'],
    package_data={'cafy_pytest': ['resources/*']},
    version=__version__,
    url='https://github.com/cafykit/cafy-pytest',
    description='Pytest Cafy Plugin', 	
    install_requires=[
        'allure-pytest',
        'jinja2',
        'pytest>=2.3',
        'PyYAML',
        'remote-pdb',
        'requests',
        'tabulate',
        'urllib3',
        'validators',
    ],
    # the following makes a plugin available to pytest
    entry_points={
        'pytest11': ['cafy_pytest = cafy_pytest.plugin']
    },
    # custom PyPI classifier for pytest plugins
    classifiers=[
        "Framework :: Pytest",
    ],
)
