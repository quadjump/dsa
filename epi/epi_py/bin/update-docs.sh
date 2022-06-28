#!/bin/sh

# From anywhere within project
pushd $(git rev-parse --show-toplevel)/epi/epi_py

poetry run sphinx-autobuild docs docs/_build/html

# doc2dash \
#   --name dsa-epi \
#   --destination ./docs/ \
#   --verbose

popd

