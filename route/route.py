from flask import Blueprint

from route import auth
from route import user

index_bp = Blueprint('index', __name__, url_prefix='/')


@index_bp.route('/')
def index():
    return 'Index'


def resister_routes(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(user.user_bp)
