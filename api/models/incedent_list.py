from api.models.models import User
from flask import Flask, jsonify
import json

incident_list = []

class Incident:

    def __init__(self):
        self.incident_list = incident_list

    def create_incedent(self, incident_id, created_on, type, location,
                        status, image, videos, comment):
        
        incident = {
            "incident_id":len(self.incident_list)+1,
            "created_on":"date",
            "type":type,
            "location":location,
            "status":status,
            "image":image,
            "videos":videos,
            "comment":comment
        }
        incident_list.append(incident)

    def retreave_all_incidents(self):
        return self.incident_list


    def delete(self):
        pass
