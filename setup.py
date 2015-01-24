from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='church_ministry',
    version=version,
    description='This app id for manage church ministry',
    author='New Indictrans Technologies Pvt. Ltd.',
    author_email='gangadhar.k@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
