from flask import Flask, jsonify, request, json
from api import app
from api.controllers.incident_controllers import IncidentsController

incidents_controller = IncidentsController()
@app.route('/api/v1/red-flags',methods=['GET'])
def fetch_red_flags():
    return incidents_controller.fetch_all_redflags()

@app.route('/api/v1/red-flags/<int:_id>', methods = ['GET'])
def fetch_single_red_flag(_id):
    return incidents_controller.fetch_specific_redflag(_id)

@app.route('/api/v1/red-flags',methods=['POST'])
def add_red_flag():
    request_data=request.get_json()
    return incidents_controller.add_redflag(request_data)

@app.route('/api/v1/red-flags/<int:_id>',methods=['DELETE'])
def delete_redflag(_id):
    return incidents_controller.delete_redflag(_id)

@app.route('/api/v1/red-flags/<int:_id>/comment', methods=['PATCH'])
def patch_redflag_comment(_id):
    return incidents_controller.patch_redflag_comment(_id)

@app.route('/api/v1/red-flags/<int:_id>/location', methods=['PATCH'])
def patch_redflag_location(_id):
    return incidents_controller.patch_redflag_location(_id)
