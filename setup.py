import pathlib

from setuptools import setup

ROOT = pathlib.Path(__file__).parent

README = (ROOT / "README.md").read_text()

setup(
    name="py-coincap-client",
    version="1.0.0",
    description="CoinCap API wrapper",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nlnsaoadc/py-coincap",
    author="nlnsaoadc",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["coincap"],
    include_package_data=True,
    install_requires=["requests"],
)
