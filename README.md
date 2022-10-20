# rest-service-dron-delivery
Install

pip3 install pipenv
pipenv  install --skip-lock  flask Flask-SQLAlchemy flask-marshmallow marshmallow-sqlalchemy marshmallow

Load init database

./bootstrap.sh load

Execute main API

./bootstrap.sh app
