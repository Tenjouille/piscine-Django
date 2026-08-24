#!/bin/bash

VENV="$HOME/.venvs/$(basename "$(pwd)")_venv"
PyPath="/usr/bin/python3"

$PyPath -m venv $VENV

source $VENV/bin/activate

pip install --force-reinstall -r requirements.txt