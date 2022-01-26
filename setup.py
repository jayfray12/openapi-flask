# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Feedback 360 Survey API",
    author_email="appdevpractice@redhat.com",
    url="",
    keywords=["OpenAPI", "Feedback 360 Survey API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This API specification contains information around the Feedback 360 Survey API developed by the App Dev Practice.  The Feedback 360 Survey API enables the management of feedback surveys for customer engagements. A feedback survey is N/A to 5 point scale of competency around the technologies used for a project. Each added employee will be able to enhance the survey by adding technologies, softskills, and freetext for each of his or her colleagues. The will enable Red Hat to better understand multiple aspects of a consultant&#39;s skillset. 
    """
)

