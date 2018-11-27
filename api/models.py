import re

class Users:
    def user(self):
        self.id = id,
        self.name = name,
        self.email = email,
        self.phoneNumber = phoneNumber,
        self.username = username,
        self.password = password

    def check_user_exist(self):
        if username != None:
            return 'Username is taken.'
        if email != None:
            return 'Email already has an account.'

    def validate_input(self):			
        if (self.isspace()) == True:
            return 'Fields can not be left empty.'
			    
    @staticmethod
    def login_validate(username, password):
        if not username or username.isspace():
            return 'Username field can not be left empty.'
        elif not password or password.isspace():
            return 'Password field can not be left empty.'
