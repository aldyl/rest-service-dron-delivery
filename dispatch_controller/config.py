#!/bin/pyton3
from flask import Flask

from flask_apscheduler import APScheduler

from dispatch_controller.model.connection import DbConnection

app = Flask(__name__)

app.app_context().push()

connection = DbConnection(app)

db = connection.get_sql_alchemy()
db_uri = connection.get_sqlite_url()
ma = connection.get_marshmallow()

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()