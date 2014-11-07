import os
import re
from cyanite import __version__
from setuptools import setup, find_packages

setup(
    name='cyanite-utils',
    version=__version__,
    author="Chris Maxwell",
    author_email="chris@wrathofchris.com",
    description="Cyanite Utils",
    url = "https://github.com/WrathOfChris/cyanite-utils",
    download_url = 'https://github.com/WrathOfChris/cyanite-utils/tarball/0.0.1',
    license="Apache",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'cassandra-driver'
    ],
    entry_points={
        "console_scripts": [
            "cyanite-list = cyanite.cli:cyanite_list",
            "cyanite-prune = cyanite.cli:cyanite_prune",
            "cyanite-delete = cyanite.cli:cyanite_delete"
        ]
    }
)
