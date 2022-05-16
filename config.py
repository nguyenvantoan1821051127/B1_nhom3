import os


class Config(object):
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cannot-be-guess'

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:nguyentoan@127.0.0.1:5432/B1_nhom3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
