from flask import Blueprint, jsonify

from infra.db import engine
from repository.UserEntity import User, Address
from sqlalchemy.orm import Session

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/user')
def user():
    execute(engine)
    return 'user'


@user_bp.route('/user/<user_id>')
def find_user_by_id(user_id):
    with Session(engine) as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user is None:
            return jsonify(message="error", data="User not found", status=404)
        return jsonify(message="ok", data=user.to_dict(), status=200)


def execute(engine):
    with Session(engine) as session:
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )
        sandy = User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        )
        patrick = User(name="patrick", fullname="Patrick Star")
        session.add_all([spongebob, sandy, patrick])
        session.commit()
