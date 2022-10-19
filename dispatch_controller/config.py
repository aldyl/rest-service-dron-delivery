#!/bin/pyton3
from flask import Flask
from dispatch_controller.DB.alchemy_marshmallow import DbConnection

app = Flask(__name__)

app.app_context().push()

connection = DbConnection(app)

db = connection.get_sql_alchemy()
db_uri = connection.get_sqlite_url()
ma = connection.get_marshmallow()

