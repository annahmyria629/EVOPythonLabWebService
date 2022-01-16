import os


class Config(object):
    TESTING = False
    SECRET_KEY = os.urandom(32)
    DATABASE_URI = "sqlite:///workdb.db"
