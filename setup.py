import sys
from setuptools import setup, find_packages

setup(
    name='imhotep_bandit',
    version='0.0.4',
    author="Dan Palmer",
    author_email="dan@danpalmer.me",
    description="An imhotep plugin for eslint",
    license='MIT',
    url='https://github.com/danpalmer/imhotep-bandit',
    packages=find_packages(),
    install_requires=[
        'imhotep>=1.0.1',
        'bandit>=1.1.0',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'imhotep_linters': [
            '.py = imhotep_bandit.plugin:Bandit',
        ],
    },
)
