# Import neccessary depencies
# From the module or framework, we import the class datatype.
# Using requst to add and access data
# Using jsonify to generate JSON data
from api.models.incident_models import Incident
from api.validations.incident_validations import Validate
from flask import jsonify, request

incident_models = Incident()

# Defining controller class for incidents
class IncidentsController:

    def __init__(self):
        # Create a list to save the information generated
        self.incidents = []

    def add_redflag(self,args):
        redflag = incident_models.create_incident(args)
        if not redflag:
            return jsonify({"message":"No incidents found"}),204
        return jsonify ({"status":201,"red-flag":redflag}),201

    def get_specific_redflag(self,incident_id):
        redflag = incident_models.get_an_incident(incident_id)
        if not redflag:
            return jsonify({"status":204,"message": "Given ID is out of range"}),204
        return jsonify({"status":200,"data":redflag}),200
    
    def get_all_redflags(self):
        incidents = incident_models.get_incidents()
        if not incidents or len(incidents) < 1 :
            return jsonify({"status":204,"message": "No Incidents available"}),204
        return jsonify({"status":200,"data":incidents})

    def patch_redflag_comment(self,incident_id):
        redflag = incident_models.get_an_incident(incident_id)
        data = request.get_json()
        if redflag:
            comment = data.get('comment')
            new_comment = comment
            redflag["comment"] = new_comment
            return jsonify({"incident":redflag})
        else:
            return jsonify({"status": 204,
                "message": "Given ID is out of range"}),204

    def patch_redflag_location(self, incident_id):
        redflag = incident_models.get_an_incident(incident_id)
        data = request.get_json()
        if redflag:
            location = data.get('location')
            new_location = location
            redflag["location"] = new_location
            return jsonify({"incident": redflag})
        else:
            return jsonify({"status": 204,"message": "Given ID is out of range"}), 204

    def delete_redflag(self,incident_id):
        redflag = incident_models.get_an_incident(incident_id)
        incidents = incident_models.get_incidents()
        if redflag:
            incidents.remove(redflag)
            return jsonify({"status":200,"data":f'{redflag} item has been deleted'}),200
        return jsonify({"status":204,"message": "Given ID is out of range"}),204

