#!/bin/bash

VENV_DIR="local_lib"
PATH_GIT_URL="https://github.com/jaraco/path.git"
PATH_LOG="path_install.log"
PY_PROG="my_program.py"

python3 -m venv ../$VENV_DIR
source $VENV_DIR/bin/activate

echo -e "\033[1mPIP Version:\033[0m\033[32m"

python3 -m pip --version
echo -e "\033[0m"

python3 -m pip install --force-reinstall git+$PATH_GIT_URL --log $PATH_LOG

python3 $PY_PROG
