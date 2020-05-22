# Contributing

This guide explains how to contribute to this project.

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## Installation

The following tools are used on the project. Install them: 

```
pip install autopep8 pytest pylint
```

Install the dependencies and use the editable mode:

```
pip install -e .
```

## Merge requests

### Branches

The name of a branch must be of the form:
* feature/* for any contribution.

### Commits

The commits must be squashed before merging with the master branch. The resulting commit must follow [this convention](https://www.conventionalcommits.org/en/v1.0.0/).

## Creating distribution archives

```
pip install --upgrade setuptools wheel
```

Create the distributions:

```
python3 setup.py sdist bdist_wheel
```

It will create a built distribution (.whl) and a source distribution (.tar.gz) in the dist folder:

```
dist/
  bookmarks-0.0.0-py3-none-any.whl
  bookmarks-0.0.0.tar.gz
```

For further information about creating archives with python, you can check [this official documentation](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives).
