class User:
    
    def __init__(self, id, firstname,lastname,
                othername, email, phone_number, username,
                registered, is_admin):

        self.id = id 
        self.fistname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email 
        self.phone_number = phone_number
        self.username = username 
        self.registered = registered
        self.is_admin = is_admin



class Incident:
    def __init__(self, incident_id, created_on, type, location,
                status, image, videos, comment):
        self.incident_id = incident_id
        self.created_on = created_on
        self.type = type 
        self.location = location
        self.status = status 
        self.image = image
        self.videos = videos
        self.comment = comment