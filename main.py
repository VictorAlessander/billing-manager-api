from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from db.config import configure
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
setup_database = configure(app)
db = SQLAlchemy(setup_database)

@app.before_first_request
def create_tables():
  db.create_all()

import models, resources

api.add_resource(resources.Index, '/')
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')