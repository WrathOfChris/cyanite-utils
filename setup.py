import os
import re
from cyanite_utils import __version__
from setuptools import setup, find_packages

setup(
    name='cyanite-utils',
    version=__version__,
    author="Chris Maxwell",
    author_email="chris@wrathofchris.com",
    description="Cyanite Utils",
    url = "https://github.com/WrathOfChris/cyanite-utils",
    download_url = 'https://github.com/WrathOfChris/cyanite-utils/tarball/%s' % __version__,
    license="Apache",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'futures',
        'six',
        'blist',
        'lz4',
        'cassandra-driver'
    ],
    entry_points={
        "console_scripts": [
            "cyanite-list = cyanite_utils.cli:cyanite_list",
            "cyanite-prune = cyanite_utils.cli:cyanite_prune",
            "cyanite-delete = cyanite_utils.cli:cyanite_delete"
        ]
    }
)
