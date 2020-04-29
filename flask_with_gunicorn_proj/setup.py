from setuptools import setup, find_packages
from codecs import open
from os import path

import versioneer

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

version=versioneer.get_version()
packages=find_packages(exclude=['docs', 'tests*'])
print(f"Creating new version: {version}")
print(f"Including the following packages")
print("=" * 80)
for package in packages:
    print(f"  + {package}")
print("=" * 80)

setup(
    name='flask_web_app',
    version=version,
    cmdclass=versioneer.get_cmdclass(),
    description='package that can be installed with pip.',
    long_description=long_description,
    url='https://zxgit.zetaglobal.io/data-cloud/dc-activity-service.git',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=packages,
    author='Krishnaiah Darla',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='darla.krishna@gmail.com')
