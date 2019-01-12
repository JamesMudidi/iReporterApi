'''
Import neccessary depencies
From the module or framework, we import the class datatype.
Using requst to add and access data
Using jsonify to generate JSON data
'''
from api.models.incident_model import Incident, Redflag, Intervention
from flask import jsonify, request

incident_model = Incident()

class IncidentsController:
    def __init__(self):
        self.incidents = []

    def add_Incident(self,args):
        Incident=incident_model.create_incident(args)
        if not Incident:
            return jsonify({
                'message':'No Incident found'
            }),200
        return jsonify ({
            'status':201,
            'Incident':Incident
        }),201

    def get_all_incidents(self):
        incidents=incident_model.get_incidents()
        if not incidents or len(incidents) < 1 :
            return jsonify({
                'status':200,
                'message':'Incident does not exist'
            }),200
        return jsonify({
            'status':200,
            'data':incidents
        })

    def fetch_specific_redflag(self,_id):
        redflag=incident_model.get_an_incident(_id)
        if not redflag:
            return jsonify({
                'status':200,
                'message':'Out of range red-flag does not exist'
            }),200
        return jsonify({
            'status':200,
            'data':redflag
        }),200
    
    def delete_redflag(self,_id):
        redflag=incident_model.get_an_incident(_id)
        incidents= incident_model.get_incidents()
        if redflag:
            incidents.remove(redflag)
            return jsonify({
                'status':200,
                'data':f'{redflag} item has been deleted'
            }),200
        return jsonify({
            'status':200,
            'message':'red-flag does not exist'
        }),200

    def patch_redflag_comment(self,_id):
        redflag=incident_model.get_an_incident(_id)
        data = request.get_json()
        if redflag:
            comment = data.get('comment')
            new_comment = comment
            redflag['comment'] = new_comment
            return jsonify({'incedent':redflag})
        else:
            return jsonify({
            'status':200,
            'message':'red-flag does not exist'
            }),200

    def patch_redflag_location(self, _id):
        redflag = incident_model.get_an_incident(_id)
        data = request.get_json()
        if redflag:
            location = data.get('location')
            new_location = location
            redflag['location'] = new_location
            return jsonify({'incedent': redflag})
        else:
            return jsonify({
                'status': 200,
                'message':'red-flag does not exist'
            }), 200
