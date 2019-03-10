from flask_restful import Resource, reqparse
from models import UserModel

parser = reqparse.RequestParser()

parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class Index(Resource):
  def get(self):
    return {'message': 'Index path'}


class UserRegistration(Resource):
  def post(self):
    data = parser.parse_args()

    new_user = UserModel(
      username=data['username'],
      password=UserModel.generate_hash(data['password'])
    )

    try:
      if UserModel.find_by_username(data['username']):
        return {'message': 'User {} already exists'.format(data['username'])}
      else:
        new_user.save()
        return {'message': 'User {} successfully created'.format(data['username'])}
    except Exception as err:
      return {'message': 'Something is wrong'}, 500


class UserLogin(Resource):
  def post(self):
    data = parser.parse_args()
    
    user = UserModel.find_by_username(data['username'])
    
    if user and UserModel.verify_hash(data['password']) == user.password:
      return {'message': 'User {} successfully logged in'.format(user.username)}
    elif not user:
      return {'message': 'User not found'}
    else:
      return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
  def post(self):
    return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
  def post(self):
    return {'message': 'User refresh'}


class TokenRefresh(Resource):
  def post(self):
    return {'message': 'Token refresh'}


class AllUsers(Resource):
  def get(self):
    return UserModel.return_all_users()

  def delete(self):
    return UserModel.delete_all_users()


class SecretResource(Resource):
  def get(self):
    return {
      'answer': 42
    }