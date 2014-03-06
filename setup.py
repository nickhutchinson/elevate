from setuptools import setup, find_packages
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="elevate",
    version='0.1dev',
    description="Poor man's sudo for Windows",
    long_description=long_description,
    
    url='http://github.com/nickhutchinson/elevate',
    author='Nick Hutchinson',
    author_email='hello@nickhutchinson.me',
    
    license='MIT',
    
    keywords=['sudo', 'win32'],
    
    packages=find_packages(),
    install_requires=[],
    
    package_data={},
    entry_points={
        'console_scripts': [
            'elevate=elevate.elevate:main',
        ],
    },
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
    ],
)