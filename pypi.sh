#!/usr/bin/env sh

python setup.py sdist bdist_wheel
ls -a
#twine upload -u "${{ PYPI_USER }}" -p "${{ PYPI_PSWD }}" --repository-url "${{ PYPI_URL }}" dist/*
