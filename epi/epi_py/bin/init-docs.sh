#!/bin/sh

# From anywhere within project
pushd $(git rev-parse --show-toplevel)/epi/py
poetry run python -m sphinx.quickstart
popd

