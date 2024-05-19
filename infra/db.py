from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

import config

engine = None
DB_Model = None
DB_Session = None

DIALECT = 'mysql'
DRIVER = 'pymysql'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True


def init(app):
    global engine
    global DB_Model
    global DB_Session
    uri = f'{DIALECT}+{DRIVER}://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_SCHEMA}'
    engine = create_engine(uri, echo=True)