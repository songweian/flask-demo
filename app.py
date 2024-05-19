import logging

from flask import Flask
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from infra import db
from middleware import middleware
from repository.UserEntity import Base

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    # Set up the logger
    handler = logging.FileHandler('app.log')  # Log to a file
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Log with a custom format
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    db.init(app)
    MetaData("flask-demo").create_all(db.engine)
    Base.metadata.create_all(db.engine)

    from route import route
    route.resister_routes(app)

    middleware.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
