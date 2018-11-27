import re

class Users:
    def user(self):
        self.id = id,
        self.name = name,
        self.email = email,
        self.phoneNumber = phoneNumber,
        self.username = username,
        self.password = password


    @staticmethod
    def login_validate(username, password):
        if not username or username.isspace():
            return 'Username field can not be left empty.'
        elif not password or password.isspace():
            return 'Password field can not be left empty.'
