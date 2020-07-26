#!/usr/bin/env bash
# exit on failure
set -e

git tag -a v"$(python setup.py --version)"
git push --tags