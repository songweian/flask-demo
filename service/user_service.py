from repository.UserEntity import User


def find_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()