import sys

from setuptools import setup
from setuptools_rust import Binding, RustExtension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rusty_sieve",
    version="0.1.0",
    rust_extensions=[RustExtension("rusty_sieve.rusty_sieve", binding=Binding.RustCPython)],
    packages=["rusty_sieve"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TomMonks/rusty-sieve",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6.9',
)