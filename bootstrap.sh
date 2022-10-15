#!/bin/bash

export FLASK_APP=./dispatch_controller/index.py

pipenv run flask --debug run -h 0.0.0.0
