# rest-service-dron-delivery

# Install

1. Clone the code from gitlab.
2. Install python3

`pip3 install pipenv`

`pipenv  install --skip-lock  flask Flask-SQLAlchemy flask-marshmallow marshmallow-sqlalchemy marshmallow flask-apscheduler`

# Excecute
1- Load the database

`./bootstrap.sh load`

2- Run Flask-SQLAlchemy-Marshmallow REST API

`./bootstrap.sh app`

# Methods and Endpoints
| ENDPOINT              | POST | GET | PUT |
| --------------------- |------| --- | ----|
| /drones               |  X   |  X  |  X  |
| /drones/<dron_id>     |      |  X  |     | 
| /medications          |  X   |  X  |  X  |
| /medications/<med_id> |      |  X  |     |
