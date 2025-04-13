from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="corefinder",
    version="1.1.7",
    author="Soumyajit Basu",
    author_email="soumyajit.basu62@gmail.com",
    description="A module for my digital business card",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Corefinder89/corefinder",
    packages=['app'],
    include_package_data=True,
    entry_points={"console_scripts": ["corefinder=app.main:main"]},
    zip_safe=False,
    python_requires=">=3.6",
    license="License :: OSI Approved :: MIT License",
    classifiers=["Programming Language :: Python"]
)
