import re

class Users:
    def user(self):
        self.email = email,
        self.username = username,
        self.password = password

    def check_user_exist(self):
        if username != None:
            return 'Username is taken.'

    def validate_input(self):			
        if not username or username.isspace():
            return 'Username field can not be left empty.'
    
    @staticmethod
    def login_validate(username):
        if not username or username.isspace():
            return 'Username field can not be left empty.'
