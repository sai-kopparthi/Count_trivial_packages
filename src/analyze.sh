#!/bin/bash

set -e
CODE_DIR="/analysis/inputs/public/source-code"

cd ${CODE_DIR}

find . -name '*.js' | xargs python3 /analyzer/white.py
