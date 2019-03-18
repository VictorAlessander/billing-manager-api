from main import db
from passlib.hash import pbkdf2_sha256 as sha256

class User(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)
  debits = db.relationship('Debit', backref='user', lazy=True)

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def generate_hash(password):
    return sha256.hash(password)

  @staticmethod
  def verify_hash(password, hash):
    return sha256.verify(password, hash)

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()

  @classmethod
  def return_all_users(cls):
    def to_json(arg):
      return {
        'username': arg.username,
        'password': arg.password
      }

    return {'users': list(map(lambda x: to_json(x), User.query.all()))}

  @classmethod
  def delete_all_users(cls):
    try:
      rows_deleted = db.session.query(cls).delete()
      db.session.commit()

      return {'message': '{} rows deleted'.format(rows_deleted)}
    except Exception as err:
      print(err)
      return {'message': 'Something went wrong'}, 500


class RevokedTokenUser(db.Model):

  __tablename__ = 'revoked_tokens'

  id = db.Column(db.Integer, primary_key=True)
  jti = db.Column(db.String(120))

  def add(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def is_jti_blacklisted(cls, jti):
    query = cls.query.filter_by(jti=jti).first()
    return bool(query)


class Category(db.Model):

  __tablename__ = 'categories'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  debits = db.relationship('Debit', backref='category', lazy=True)

  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def return_all_categories(cls):
    def to_json(arg):
      return {
        'id': arg.id,
        'name': arg.name
      }

    return {'categories': list(map(lambda x: to_json(x), Category.query.all()))}


class Debit(db.Model):

  __tablename__ = 'debits'

  id = db.Column(db.Integer, primary_key=True)
  debit_name = db.Column(db.String(100), nullable=False)
  cost = db.Column(db.Float, nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  @classmethod
  def find_debits_by_user(cls, username):
    def to_json(arg):
      return {
        "id": arg.id,
        "debit_name": arg.debit_name,
        "cost": arg.cost,
        "category_id": arg.category_id,
        "user_id": arg.user_id
      }

    return {'debits': list(map(
      lambda x: to_json(x), Debit.query.filter_by(user_id=username.id)))}
