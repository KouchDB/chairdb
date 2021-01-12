#!/bin/bash

flake8 microcouch tests --max-complexity=5
python -m pytest --cov=microcouch --cov=tests --cov-report html --cov-branch -vv
