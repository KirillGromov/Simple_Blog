class Configuration():
   DEBUG = True
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://womorg:1234@localhost/test1'
   SECRET_KEY = 'secret key'

   ### Flask-security###
   SECURITY_PASSWORD_SALT = 'salt'
   SECURITY_PASSWORD_HASH = 'sha512_crypt'