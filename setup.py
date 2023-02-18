from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="subregapi",
    version="0.1.0",
    author="David Hrbáč",
    author_email="david+pypi@hrbac.cz",
    description="Python client for Subreg.cz API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/subregapi",
    packages=["subregapi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests"
    ]
)

