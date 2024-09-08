from app.exceptions.exception import UserExistError
from app.schemas.user import UserPassword
from app.models.user import User
from app.services.auth import hashing
from app.services.auth.grant import create_token_response_from_user


class CreateUser:

    def __init__(self, request_data: UserPassword):
        self.request_data = request_data

    def respond(self):
        user = User.get_or_none(User.username == self.request_data.username)
        if user:
            raise UserExistError('The username already exists')
        password = hashing.get_password_hash(self.request_data.password)
        user = User.create(username=self.request_data.username, password=password)
        return User.get_or_none(User.id == user.id)


class ModifyUser:

    def __init__(self, request_data: UserPassword):
        self.request_data = request_data

    def respond(self):
        user = User.get_or_none(User.username == self.request_data.username)
        if not user:
            raise UserExistError('The username already exists')
        password = hashing.get_password_hash(self.request_data.password)
        user.password = password
        user.save()
        return user
