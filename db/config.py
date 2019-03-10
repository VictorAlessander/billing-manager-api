
def configure(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///billing.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SECRET_KEY'] = 'ef5bcb77da527eb6901dcaf2ad046e3cab938983b71d6d1c'

  return app