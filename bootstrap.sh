#!/bin/bash

[ "$1" == "app" ] &&export FLASK_APP=./dispatch_controller/app.py
[ "$1" == "load_bd" ] && export FLASK_APP=./dispatch_controller/load_db
#[ "$1" == "test" ] && export FLASK_APP=./dispatch_controller/test.py

pipenv run flask --debug run -h 0.0.0.0
