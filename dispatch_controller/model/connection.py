import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

class DbConnection():
    
    def  __init__(self, app) -> None:

        self.basedir = os.path.abspath(os.path.dirname(__file__))

        # Build the Sqlite ULR for SqlAlchemy
        self.sqlite_url = "sqlite:///" + os.path.join(self.basedir, "dispatch.db")

        # Configure the SqlAlchemy part of the app instance
        app.config["SQLALCHEMY_ECHO"] = True  # Set False for producction
        app.config["SQLALCHEMY_DATABASE_URI"] = self.sqlite_url
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        # Create the SqlAlchemy db instance
        self.db = SQLAlchemy(app)

        # Initialize Marshmallow after creating SQLAlchemy
        self.marshmallow = Marshmallow(app)

    def get_sqlite_url(self):
        return self.sqlite_url

    def get_sql_alchemy(self):
        return self.db
    
    def get_marshmallow(self):
        return self.marshmallow