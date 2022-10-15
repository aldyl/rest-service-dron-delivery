#!/bin/bash

export FLASK_APP=./drones.index.py

pipenv run flask --debug run -h 0.0.0.0
