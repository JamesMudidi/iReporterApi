'''
Import relevant dependencies
datetime for the date and time
'''
from flask import jsonify
import datetime

# Create a list to save the created incidents
incidents=[]
redflags=[]
interventions=[]

# Defining model class for incidents
class Incident:
    def __init__(self):
        self.incidents=incidents

    def create_incident(self,args):
        incident=dict(
            incidentId=len(incidents)+1,
            createdOn=datetime.datetime.now(),
            createdBy=args['createdBy'],
            incidentType=args['incidentType'],
            location=geocoder.ip('me'),
            status=args['status'],
            image=args['image'],
            video=args['video'],
            comment=args['comment']
        )
        self.incidents.append(incident)
        return incident

    def get_incidents(self):
        return self.incidents

    def get_an_incident(self,incidentId):
        for incident in self.incidents:
            if incident['incidentId']==incidentId:
                return incident

# Defining model class for the Redflag and inheriting the incident class
class Redflag(Incident):
    def __init__(self):
        self.redflags=redflags

        super().__init__(args)
        redflag=dict(
            incidentType=Redflag
        )
        self.redflags.append(redflag)
        return redflag

    def get_redflags(self,incidentType):
        for incident in self.incidents:
            if incident['incidentType']==Redflag:
                return incident

    def get_a_redflag(self,incidentId):
        for redflag in self.redflags:
            if redflag['incidentId']==incidentId:
                return redflag


# Defining model class for the Redflag and inheriting the incident class
class Intervention(Incident):
    def __init__(self):
        self.incidents=incidents

        super().__init__(args)
        intervention=dict(
            incidentType=Intervention
        )
        self.interventions.append(intervention)
        return intervention

    def get_interventions(self,incidentType):
        for incident in self.incidents:
            if incident['incidentType']==Intervention:
                return incident

    def get_an_intervention(self,incidentId):
        for intervention in self.interventions:
            if intervention['incidentId']==incidentId:
                return intervention
