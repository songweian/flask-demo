from flask import Flask
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from infra import db
from repository.UserEntity import Base


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init(app)
    MetaData("flask-demo").create_all(db.engine)
    Base.metadata.create_all(db.engine)

    from route import route
    route.resister_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
