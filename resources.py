from flask_restful import Resource, reqparse
from models import RevokedTokenUser, User, Category, Debit
from flask_jwt_extended import (
  create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
  )

# parser.add_argument('username', help = 'This field cannot be blank', required = True)
# parser.add_argument('password', help = 'This field cannot be blank', required = True)

class Index(Resource):
  def get(self):
    return {'message': 'Index path'}


class UserRegistration(Resource):

  def __init__(self):
    self.parser = reqparse.RequestParser()

    self.parser.add_argument(
      'username',
      help='Username name cannot be blank',
      required=True,
      location='json'
    )
    self.parser.add_argument(
      'password',
      help='Password name cannot be blank',
      required=True,
      location='json'
    )

  def post(self):
    data = self.parser.parse_args()

    new_user = User(
      username=data['username'],
      password=User.generate_hash(data['password'])
    )

    try:
      if User.find_by_username(data['username']):
        return {'message': 'User {} already exists'.format(data['username'])}
      else:
        new_user.save()
        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])
        return {
          'message': 'User {} successfully created'.format(data['username']),
          'access_token': access_token,
          'refresh_token': refresh_token
          }
    except Exception as err:
      return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):

  def __init__(self):
    self.parser = reqparse.RequestParser()

    self.parser.add_argument(
      'username',
      help='Username name cannot be blank',
      required=True,
      location="json"
    )
    self.parser.add_argument(
      'password',
      help='Password name cannot be blank',
      required=True,
      location="json"
    )

  def post(self):
    data = self.parser.parse_args()

    user = User.find_by_username(data['username'])

    if user and User.verify_hash(data['password'], user.password):
      access_token = create_access_token(identity=data['username'])
      refresh_token = create_refresh_token(identity=data['username'])
      return {
        'message': 'User {} successfully logged in'.format(user.username),
        'access_token': access_token,
        'refresh_token': refresh_token
        }
    elif not user:
      return {'message': 'User not found'}
    else:
      return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
  @jwt_required
  def post(self):
    jti = get_raw_jwt()['jti']

    try:
      revoked_token = RevokedTokenUser(jti)
      revoked_token.add()

      return {'message': 'Access Token has been revoked'}
    except Exception as err:
      print(err)
      return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
  @jwt_refresh_token_required
  def post(self):
    jti = get_raw_jwt()['jti']

    try:
      revoked_token = RevokedTokenUser(jti)
      revoked_token.add()

      return {'message': 'Refresh Token has been revoked'}
    except Exception as err:
      print(err)
      return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
  @jwt_refresh_token_required
  def post(self):
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return {'access_token': access_token}


class AllUsers(Resource):
  @jwt_required
  def get(self):
    return User.return_all_users()

  @jwt_required
  def delete(self):
    return User.delete_all_users()


class SecretResource(Resource):
  def get(self):
    return {
      'answer': 42
    }


class CategoryResource(Resource):

  def __init__(self):
    self.parser = reqparse.RequestParser()

    self.parser.add_argument(
      'name',
      help='Name cannot be blank',
      required=True,
      location="json"
    )

  def get(self):
    return Category.return_all_categories()

  @jwt_required
  def post(self):
    data = self.parser.parse_args()

    category = Category(name=data['name'])

    try:
      category.save()

      return {'message': 'Category {} successfully created'.format(data['name'])}
    except Exception as err:
      print(err)
      return {'message': 'Something went wrong'}


class DebitResource(Resource):

  def __init__(self):
    self.parser = reqparse.RequestParser()

    # self.parser.add_argument(
    #   'debit_name', help='Debit name cannot be blank', required=True
    # )
    # self.parser.add_argument(
    #   'cost', help='Cost cannot be blank', required=True
    # )
    # self.parser.add_argument(
    #   'category_id', help='Category id cannot be blank', required=True
    # )

  def get(self):
    self.parser.add_argument(
      'user', help='User id cannot be blank', required=True
    )

    data = self.parser.parse_args()

    try:
      debits = Debit.find_debits_by_user(int(data['user']))

      return debits
    except Exception as err:
      print(err)
      return {'message': 'Something went wrong'}

  def post(self):
    self.parser.add_argument(
      'debit_name',
      help='Debit name cannot be blank',
      required=True,
      location="json"
    )
    self.parser.add_argument(
      'cost',
      help='Cost cannot be blank',
      required=True,
      location="json"
    )
    self.parser.add_argument(
      'category_id',
      help='Category id cannot be blank',
      required=True,
      location="json"
    )
    self.parser.add_argument(
      'user_id',
      help='User id cannot be blank',
      required=True,
      location="json"
    )

    data = self.parser.parse_args()

    try:
      debit = Debit(
        debit_name=data['debit_name'],
        cost=data['cost'],
        category_id=data['category_id'],
        user_id=data['user_id']
      )

      debit.save()

      return {'message': 'Debit was successfully saved'}
    except Exception as err:
      print(err)
      return {'message': 'Something went wrong'}
