# Import neccessary depencies
# From the module or framework, we import the class datatype.
# Using requst to add and access data
# Using jsonify to generate JSON data
# Using json for reading JSON data
from flask import Flask, jsonify, request, json
from api.controllers.incident_controllers import IncidentsController
from api import app

incident_controller = IncidentsController()

class incident_views:
    # Route for creating an incident
    @app.route('/api/v1/incidents',methods=['POST'])
    def add_redflag():
        request_data=request.get_json()
        return incident_controllers.add_redflag(request_data)

    # Route for selecting a single incident
    @app.route('/api/v1/incidents/<int:_id>', methods = ['GET'])
    def get_single_redflag(_id):
        return incident_controllers.get_specific_redflag(_id)

    # Route for selecting all incidents
    @app.route('/api/v1/incidents',methods=['GET'])
    def get_redflags():
        return incident_controllers.get_all_redflags()

    # Route for changing an incident's comment
    @app.route('/api/v1/incidents/<int:_id>/comment', methods=['PATCH'])
    def patch_redflag_comment(_id):
        return incident_controllers.patch_redflag_comment(_id)

    # Route for changing an incident's location
    @app.route('/api/v1/incidents/<int:_id>/location', methods=['PATCH'])
    def patch_redflag_location(_id):
        return incident_controllers.patch_redflag_location(_id)

    # Route for deleting an incident
    @app.route('/api/v1/incidents/<int:_id>',methods=['DELETE'])
    def delete_redflag(_id):
        return incident_controllers.delete_redflag(_id)
