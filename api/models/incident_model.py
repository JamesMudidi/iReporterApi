'''
Import relevant dependencies
datetime for the date and time
'''
from flask import jsonify
import datetime
import geocoder

# Create a list to save the created incidents
incidents_list = []

# Defining model class for incidents
class Incident:
    incidents_list = []

    def __init__(self, incidentId, createdOn, createdBy, incidentType,
                location, status, images, videos, comment):
        self.incidentId=len(incidents_list)+1
        self.createdOn=datetime.datetime.now()
        self.createdBy=createdBy
        self.incidentType=incidentType
        self.location=geocoder.ip('me')
        self.status=status
        self.images=images
        self.videos=videos
        self.comment=comment

    def incident_dict(self):
        incidents = {
             "incidentId":self.incidentId,
             "createdOn":self.createdOn,
             "createdBy":self.createdBy,
             "incidentType":self.incidentType,
             "location":self.location,
             "status":self.status,
             "images":self.images,
             "videos":self.videos,
             "comment":self.comment
        }
        self.incidents_list.append(incidents)
        return jsonify({
            'status':200,
            'data':incidents,
            'message':'user successfully registered'
            })

# Defining model class for the redflag incident and inheriting the incident class
class Redflag(Incident):
    def __init__(self, incidentId, createdOn, createdBy, incidentType,
                location, status, images, videos, comment):
        super().__init__(incidentId, createdOn, createdBy,
                location, status, images, videos, comment)
        self.incidentType=Redflag

# Defining model class for the intervention incident and inheriting the incident class
class Intervention(Incident):
    def __init__(self, incidentId, createdOn, createdBy, incidentType,
                location, status, images, videos, comment):
        super().__init__(incidentId, createdOn, createdBy,
                location, status, images, videos, comment)
        self.incidentType=Intervention
