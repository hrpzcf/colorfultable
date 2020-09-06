import os

from setuptools import find_packages, setup

from colorfultable import author, author_email, name, version, website1

description = 'A module to help print beautiful table on the terminal.'
long_description = description

if os.path.exists('README.md'):
    with open('README.md', 'r', encoding='utf-8') as file:
        long_description = file.read()

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    license='MIT License',
    packages=find_packages(),
    platforms=['all'],
    url=website1,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Terminals',
        'Topic :: System :: Console Fonts',
    ],
)
