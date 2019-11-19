from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

server = Flask(__name__)
dbase = SQLAlchemy(server)

server.config['SECRET_KEY'] = 'thisisverysecret'
# server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/trash'
server.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from api.model import *
from api.api import *

dbase.create_all()