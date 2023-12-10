#!/usr/bin/env bash
set -e -o pipefail

: "${PROJECT:=lambda-example}"
: "${PYTHON_VERSION:=3.11}"

if [[ ! "$(uname -o)" =~ "Darwin" ]]; then
    >&2 echo "Script is only valid for MacOS systems."
    exit 1
fi

if ! which -s hatch 2> /dev/null ; then
    >&2 echo "Install hatch utility globally"
    >&2 echo " - brew install hatch"
    exit 1
fi

if ! which -s zip 2> /dev/null ; then
    >&2 echo "Install zip utility"
    >&2 echo " - brew install zip"
    exit 1
fi

if ! which -s jq; then
    >&2 echo "Install jq"
    >&2 echo " - brew install jq"
    exit 1
fi

if ! docker 2> /dev/null ; then
    >&2 echo "Install docker"
    >&2 echo " - brew install --cask docker"
    exit 1
fi

if ! python --version > /dev/null 2>&1 ; then
    >&2 echo "Install python ${PYTHON_VERSION}"
    >&2 echo " - brew install python@${PYTHON_VERSION}"
    exit 1
fi

if ! pip --version > /dev/null 2>&1 ; then
    >&2 echo "Install pip for python ${PYTHON_VERSION}"
    exit 1
fi

if ! which -s virtualenv > /dev/null 2>&1 ; then
    >&2 echo "Unable to locate virtualenv executable"
    >&2 echo " - brew install virtualenv"
    exit 1
fi

echo "Make sure to be in the '${PROJECT}' virtual environment."
echo "Run this command:"
echo " - hatch shell"
echo -e "\nYou are all set."
