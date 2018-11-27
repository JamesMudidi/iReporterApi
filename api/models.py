import re

class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_user_exist(self):
        if username != None:
            return 'Username is taken.'

    def validate_input(self):			
        if not username or username.isspace():
            return 'Username field can not be left empty.'
    
    def login_validate(username, password):
        if not username or username.isspace():
            return 'Username field can not be left empty.'
        elif not password or password.isspace():
            return 'Password field can not be left empty.'
