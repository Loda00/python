import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLE = True
  SECRET_KEY = 'this-really-needs-to-be-changed'
  SQLALCHEMY_DATABASE_URI = os.environ['']

class ProductionConfig(object):
  DEBUG = False

class StaginConfig(object):
  DEVELOPMENT = True
  DEBUG = True

class DevelopmentConfig(object):
  DEVELOPMENT = True
  DEBUG = True


class TestingConfig(object):
  TESTING = True
