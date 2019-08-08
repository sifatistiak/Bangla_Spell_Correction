import os
import sys
from setuptools import setup, find_packages

f = open('README.md')
readme = f.read()
f.close()

version = '0.0.1'

if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name='bengali-corrector',
    version=version,
    description='bengali-corrector is a library for Spell Correction of Bangla Word',
    long_description=readme,
    author='Istiak Ahamed',
    author_email='sifatistiak@gmail.com',
    maintainer='Istiak Ahamed',
    maintainer_email='sifatistiak@gmail.com',
    url='https://github.com/sifatistiak/Bangla_Spell_Corrector/tree/master',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Bengali',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
    ],
    zip_safe=False,
)