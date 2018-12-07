# Import relevant dependencies
# uuid for random ids and datetime for the date and time
import datetime
import uuid

# Create a list to save the created users
users = []
admins = []

# Defining model class for users
class User:
    def __init__(self):
        # Assigning information into the users list 
        self.users = users

    # Model for creating users
    # Used args to pass a variable number of arguments
    def create_user(self, args):
        user = dict(
            user_id = len(self.users)+1,
            firstname = args['firstname'],
            lastname = args['lastname'],
            othernames = args['othernames'],
            email = args['email'],
            phone_number = args['phone_number'],
            username = args['username'],
            password = args['password'],
            registered = datetime.datetime.now(),
            is_admin = False
        )
        # Adding a new user from the user dictionary to the self.users list
        self.users.append(user)
        return user

    # Model for viewing all users
    def get_users(self):
        # Returns a string containing all users
        return self.users

    # Model for viewing a specific user
    def get_one_user(self,_id):
        # checks for given id aganst all ids and
        # Returns a string containing a single user
        # with a similar id
        for user in self.users:
            if user['user_id'] == user_id:
                return user

# Defining model class for administrators
class Admin(User):
    def __init__(self):
        self.admins = admins

    # Model for creating admin users
    # Used args to pass a variable number of arguments
    def create_admin(self, args):
        admin = dict(
            admin_id = len(self.admins)+1,
            firstname = args['firstname'],
            lastname = args['lastname'],
            othernames = args['othernames'],
            email = args['email'],
            phone_number = args['phone_number'],
            username = args['username'],
            password = args['password'],
            registered = datetime.datetime.now(),
            is_admin = True
        )
        # Adding a new admin user from the admin user dictionary to the self.admins list
        self.admins.append(admin)
        return admin

