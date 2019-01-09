'''
Import neccessary depencies
From the module or framework, we import the class datatype.
Using requst to add and access data
Using jsonify to generate JSON data
Using json for reading JSON data
'''
from flask import Flask, jsonify, request, json
from api import app
from api.controllers import incident_controller

class incident_views:

    # Route for creating a redflag
    @app.route('/api/v1/incident/redflag', methods=['POST'])
    def create_redflag():
        data=request.get_json()
        return incident_controller.add_incident(data)

    # Route for creating an intervention
    @app.route('/api/v1/incident/intervention', methods=['POST'])
    def create_intervention():
        data=request.get_json()
        return incident_controller.add_incident(data)

    # Route for viewing a single redflag
    @app.route('/api/v1/incident/redflag/<incidentId>', methods=['GET'])
    def get_a_redflag():
        data=request.get_json()
        return incident_controller.get_a_redflag(data)

    # Route for viewing a single intervention
    @app.route('/api/v1/incident/intervention/<incidentId>', methods=['GET'])
    def get_an_intervention():
        data=request.get_json()
        return incident_controller.get_an_intervention(data)

    # Route for viewing all incidents
    @app.route('/api/v1/incident/incidents', methods=['GET'])
    def get_all_incidents():
        data=request.get_json()
        return incident_controller.get_all_incidents(data)

    # Route for viewing all Redflags
    @app.route('/api/v1/incident/redflags', methods=['GET'])
    def get_all_redflags():
        data=request.get_json()
        return incident_controller.get_all_redflags(data)

    # Route for viewing all Interventions
    @app.route('/api/v1/incident/interventions', methods=['GET'])
    def get_all_interventions():
        data=request.get_json()
        return incident_controller.get_all_interventions(data)

    # Route for editing Redflag location
    @app.route('/api/v1/incident/redflag/<incidentId>/location', methods=['PATCH'])
    def edit_redflag_location():
        data=request.get_json()
        return incident_controller.edit_redflag_location(data)

    # Route for editing Intervention location
    @app.route('/api/v1/incident/intervention/<incidentId>/location', methods=['PATCH'])
    def edit_intervention_location():
        data=request.get_json()
        return incident_controller.edit_intervention_location(data)

    # Route for editing Redflag comment
    @app.route('/api/v1/incident/redflag/<incidentId>/comment', methods=['PATCH'])
    def edit_redflag_comment():
        data=request.get_json()
        return incident_controller.edit_redflag_comment(data)

    # Route for editing Intervention comment
    @app.route('/api/v1/incident/intervention/<incidentId>/comment', methods=['PATCH'])
    def edit_intervention_comment():
        data=request.get_json()
        return incident_controller.edit_intervention_comment(data)

    # Route for editing Redflag status
    @app.route('/api/v1/incident/redflag/<incidentId>/status', methods=['PATCH'])
    def edit_redflag_status():
        data=request.get_json()
        return incident_controller.edit_redflag_status(data)

    # Route for editing Intervention status
    @app.route('/api/v1/incident/intervention/<incidentId>/status', methods=['PATCH'])
    def edit_intervention_status():
        data=request.get_json()
        return incident_controller.edit_intervention_status(data)

    # Route for deleting a redflag
    @app.route('/api/v1/incident/redflag/<incidentId>', methods=['DELETE'])
    def delete_redflag():
        data=request.get_json()
        return incident_controller.delete_redflag(data)

    # Route for deleting an intervention
    @app.route('/api/v1/incident/intervention/<incidentId>', methods=['DELETE'])
    def delete_intervention():
        data=request.get_json()
        return incident_controller.delete_intervention(data)