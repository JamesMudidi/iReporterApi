# Import relevant dependencies
# uuid for random ids and datetime for the date and time
import datetime
import uuid

# Create a list to save the created incidents
incidents = []

# Defining model class for incidents
class Incident:
    def __init__(self):
        # Assigning information into the incidents list 
        self.incidents = incidents

    # Model for creating redflag incidents
    # Used args to pass a variable number of arguments
    def create_incident(self, args):
        incident = dict(
            incident_id=len(self.incidents)+1,
            createdOn=datetime.datetime.now(),
            createdBy=args['createdBy'],
            incident_type=args['type'],
            location=args['location'],
            status=args['status'],
            image=args['image'],
            video=args['video'],
            comment=args['comment']
        )
        # Adding a new item from the incident dictionary to the self.incidents list
        self.incidents.append(incident)
        return incident

    # Model for viewing all redflag incidents
    def get_incidents(self):
        # Returns a string containing redflag incidents
        return self.incidents

    # Model for viewing a specific redflag incident
    def get_an_incident(self,_id):
        # checks for given id aganst all ids and
        # Returns a string containing a redflag incident
        # with a similar id
        for incident in self.incidents:
            if incident['_id'] ==_id:
                return incident