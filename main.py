from dependency_injector.providers import Singleton
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

import src
import src.resources as resources
from container import Container
from src.infrastructure.sqlalchemy.db import Base, LocalSession, engine

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "jwt-secret-string"
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]

jwt = JWTManager(app)
api = Api(app)


@app.before_first_request
def create_tables():
    Base.metadata.create_all(bind=engine)


api.add_resource(resources.Index, "/")
api.add_resource(resources.UserRegistration, "/registration")
api.add_resource(resources.UserLogin, "/login")
# api.add_resource(resources.UserLogoutAccess, "/logout/access")
# api.add_resource(resources.UserLogoutRefresh, "/logout/refresh")
api.add_resource(resources.TokenRefresh, "/token/refresh")
api.add_resource(resources.AllUsers, "/users")
api.add_resource(resources.SecretResource, "/secret")
# api.add_resource(resources.CategoryResource, "/categories")
# api.add_resource(resources.DebitResource, "/debits")


# @jwt.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
#     jti = decrypted_token["jti"]
#     return models.RevokedTokenUser.is_jti_blacklisted(jti)

container = Container(session=Singleton(LocalSession))
container.wire(packages=[src])
