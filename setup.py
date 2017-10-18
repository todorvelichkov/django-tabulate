import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version = '0.1.1'

setup(
    name='django-tabulate',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Pretty-print Django QuerySets.',
    long_description=README,
    url='https://github.com/todorvelichkov/django-tabulate',
    author='Todor Velichkov',
    author_email='todorvelichkov89@gmail.com',
    keywords='tabulate Pretty-print Django queryset',
    install_requires=[
       'django',
       'tabulate'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        "Topic :: Software Development :: Libraries"
    ],
)