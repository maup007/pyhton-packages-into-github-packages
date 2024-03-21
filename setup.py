from setuptools import setup, find_packages

setup(
    name='hello_world',
    version='1.0.0',
    packages=find_packages(),
    author='maup007',
    author_email='maup@tdc.dk',
    description='helloworld package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/maup007/pyhton-packages-into-github-packages',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
