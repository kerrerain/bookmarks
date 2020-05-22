import setuptools

NAME = "bookmarks"
VERSION = "0.0.0"
DESCRIPTION = "A module to save bookmarks."
REQUIRES = []

with open("README.md") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    install_requires=REQUIRES
)
