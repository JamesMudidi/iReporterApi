class User:
    # user class
    def __init__(self, userId, firstName, lastName, otherNames, email,
                 phoneNumber, userName, registered, isAdmin, password):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.otherNames = otherNames
        self.email = email
        self.phoneNumber = phoneNumber
        self.userName = userName
        self.registered = registered
        self.isAdmin = isAdmin
        self.password = password

    def get_user_details(self):
        # getting one user
        return {
            "userId": self.userId,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "otherNames": self.otherNames,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "userName": self.userName,
            "registered": self.registered,
            "isAdmin": self.isAdmin
        }
