'''
Import relevant dependencies
datetime for the date and time
'''
import datetime

# Create a list to save the created users
users = []

# Defining model class for users
class User:
    def __init__(self):
# Assigning information into the users list 
        self.users=users

    '''
    Model for creating users
    Used args to pass a variable number of arguments
    '''
    def add_user(self, args):
        user = dict(
        user_id=len(self.users)+1,
        firstname=args['firstname'],
        lastname=args['lastname'],
        othernames=args['othernames'],
        email=args['email'],
        phoneNumber =args['phoneNumber'],
        username=args['username'],
        password=args['password'],
        registered=datetime.datetime.now(),
        is_admin=False
        )
        # Adding a new user from the user dictionary to the self.users list
        self.users.append(user)
        return user
        
