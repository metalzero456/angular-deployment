import os.path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

basedir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
# SQL Alchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qmromzvsjcmxbk:e73238097a1a899498fb14c71ec3ad15561c773dc9b182d784757822b7bf7279@ec2-52-204-72-14.compute-1.amazonaws.com:5432/dappa617lqu7u1'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_ECHO']=True

# Set the name of api
api = Api(app, title="Movies API")
# Instantiate sql alchemy database
db = SQLAlchemy(app)

# import movies endpoints api as ns1
from api_movies.movies_routes import api as ns1
# import directors endpoints api as ns2
from api_movies.director_routes import api as ns2
# adding both namespace to main api
api.add_namespace(ns1)
api.add_namespace(ns2)

if __name__ == '__main__':
    app.run(debug=True)
