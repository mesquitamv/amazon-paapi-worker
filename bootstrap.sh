#!/bin/sh
export FLASK_APP=./products-worker/index.py

flask --debug run -h 0.0.0.0 -p 8000
