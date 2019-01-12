users = []

class User:
    def __init__(self):
        self.users = users

    def create_user(self, args):
        user = dict(
            user_id = len(self.users)+1,
            firstname = args['firstname'],
            lastname = args['lastname'],
            othernames = args['othernames'],
            email = args['email'],
            phone_number = args['phone_number'],
            username = args['username'],
            registered = args['registered'],
            is_admin = args['is_admin']
        )
        self.users.append(user)
        return user

    # def get_user(self):
    #     return self.users