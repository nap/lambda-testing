#!/usr/bin/env bash
set -e -o pipefail

: "${PYTHON_VERSION:=3.11}"

if [[ -d "dist" ]]; then
  rm -vRf dist/*
fi
[[ ! -d dist ]] && mkdir -vp dist

pip install \
    --platform=aarch64 \
    --target=dist \
    --ignore-installed \
    --implementation=cp \
    --python-version="${PYTHON_VERSION}" \
    --only-binary=:all: \
    --upgrade \
    .
cp -rv ./calculation ./dist/
find dist -iname "__pycache__" -type d -exec rm -vRf {} +
cd dist
zip -vr function.zip .
cd -
echo "done."
