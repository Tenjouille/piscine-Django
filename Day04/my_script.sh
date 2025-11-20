#!/bin/bash

VENV="django_venv"
PyPath="/usr/bin/python3"

$PyPath -m venv $VENV

source $VENV/bin/activate

pip install --force-reinstall -r requirement.txt