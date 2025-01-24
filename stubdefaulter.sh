#!/usr/bin/env bash

set -eou pipefail

mkdir google
mv google-stubs google/google
touch google/google/__init__.pyi
touch google/google/ads/__init__.pyi
uv run stubdefaulter -p google
mv google/google google-stubs
rm -rf google
rm google-stubs/__init__.pyi
rm google-stubs/ads/__init__.pyi
