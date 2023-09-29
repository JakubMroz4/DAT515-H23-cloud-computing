import os


class BaseConfig(object):
    DB_USER = os.environ['POSTGRES_USER']
    DB_PASS = os.environ['POSTGRES_PASSWORD']
    DB_PORT = os.environ['DATABASE_PORT']
    DB_NAME = os.environ['POSTGRES_DB']

    #DB_USER = "postgres"
    #DB_PASS = "postgres"
    #DB_PORT = "5432"
    #DB_NAME = "flask_db"
    DB_HOST = "db"

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    #SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:postgres@db:5432/flask_db'


pass