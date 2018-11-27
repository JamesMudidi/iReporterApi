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
        if not self.username or self.username.isspace():
            return 'Username field can not be left empty.'
			
        elif not self.phoneNumber or self.phoneNumber.isspace():
            return 'Phone Number field can not be left empty.'
			
        elif not self.email or self.email.isspace():
            return 'Email field can not be left empty.'
			
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return 'Enter a valid email address.'
			
        elif not self.password or self.password.isspace():
            return 'Password field can not be left empty.'
			
        elif len(self.password) < 4:
            return 'Password has to be longer than 4 characters.'
    
    @staticmethod
    def login_validate(username, password):
        if not username or username.isspace():
            return 'Username field can not be left empty.'
        elif not password or password.isspace():
            return 'Password field can not be left empty.'
