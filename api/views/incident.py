from flask import Flask, jsonify, request
from api.models.incident import Incident
from datetime import datetime
from api.common.validator import email, required
from marshmallow import ValidationError, Schema, fields
from api.views import api

incidents_list = []
redflags_list = []

class IncidentSchema(Schema):
    #Represents the schema for incidents
    type=fields.Str(required=True, validate=(required))
    comment=fields.Str(required=True, validate=(required))
    location=fields.Str(required=True, validate=(required))
    id=fields.Int(required=False)
    createdOn=fields.Str(required=False)
    createdBy=fields.Int(required=False)
    Images=fields.Str(required=False)
    status=fields.Str(required=False)
    Videos=fields.Str(required=False)

class RedflagSchema(Schema):
    #Represents the schema for redflags
    type=fields.Str(required=False)
    comment=fields.Str(required=True, validate=(required))
    location=fields.Str(required=True, validate=(required))
    id=fields.Int(required=False)
    createdOn=fields.Str(required=False)
    createdBy=fields.Str(required=False)
    Images=fields.Str(required=False)
    status=fields.Str(required=False)
    Videos=fields.Str(required=False)

@api.route('/incident', methods=['POST'])
def create_incident():
    # posting an incident
    data, errors = IncidentSchema().load(request.get_json())
    if errors:
            return jsonify({
              "errors": errors, 
              "status": 400}), 400

    id=len(incidents_list)+1
    createdOn=datetime.now().strftime('%d-%m-%Y %H:%M')
    incident=Incident(id, createdOn, data['createdBy'], data['type'], data['location'],
                data['status'], data['Images'], data['Videos'], data['comment'])

    incidents_list.append(incident)

    return jsonify({
        "Incident": incident,
        "message": "Incident created",
        }), 201

@api.route('/incident', methods=['GET'])
def get_incidents():
    # getting all incidents
    Incidents=[incident.get_incident() for incident in incidents_list]
    return jsonify({"data": Incidents})


@api.route('/incident/<int:incidentId>', methods=['GET'])
def get_incident(incidentId):
    one_incident=[]
    incident=incidents_list[incidentId - 1]
    one_incident.append(incident.get_incident())
    return jsonify({
        "data": one_incident
        }), 200

@api.route('/incident/<int:incidentId>', methods=['DELETE'])
def delete_incident(incidentId):
    # deleting an incident
    if incidentId==0 or incidentId > len(incidents_list):
        return jsonify({"message": "Index out of range"}), 400
    for incident in incidents_list:
        if incident.id==incidentId:
            incidents_list.remove(incident)
    return jsonify({
        "status": 200,
        "message": "incident successfully deleted"
        }), 200

@api.route('/redflag', methods=['GET'])
def get_redflags():
    # getting all redflags
    Redflags=[incident.get_incident() for incident in redflags_list]
    if len(redflags_list) > 0:
     return jsonify({
         "data": Redflags,
         "status" : 200
        }, 200)
    else:
     return jsonify({
             "error": "no redflags found",
             "status": 404
             }, 404)

@api.route('/redflag', methods=['POST'])
def create_redflag():
    # function for creating a redflag
    data, errors=RedflagSchema().load(request.get_json())    
    if errors:
            return jsonify({
              "errors": errors, 
              "status": 422}), 422

    id=len(redflags_list)+1
    createdOn=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    type="redflag"
    redflag=Incident(id, createdOn, data['createdBy'], type, data['location'],
                data['status'], data['Images'], data['Videos'], data['comment'])

    redflags_list.append(redflag)

    return jsonify({
        "message": "Redflag created",
        "status": 201,
        }), 201

@api.route('/redflag/<int:redflagId>', methods=['GET'])
def get_single_redflag(redflagId):
    # function for getting a single redflag
    one_incident=[]
    incident=redflags_list[redflagId - 1]
    one_incident.append(incident.get_incident())
    return jsonify({
        "data": one_incident
        }), 200

@api.route('/redflag/<int:redflagId>/location', methods=['PATCH'])
def edit_redflag_location(redflagId):
    # function for editing redflag location
    if redflagId==0 or redflagId > len(redflags_list):
        return jsonify({"message": "Index is out of range"}), 400
    data=request.get_json()
    for incident in redflags_list:
        if int(incident.id)==int(redflagId):
            incident.comment=data['location']
            return jsonify({
                "status": 200,
                "message": "redflag updated"
                }), 200
        else:
         return jsonify({
             "error": "the redflag was not found",
             "status": 404
             }, 404)

@api.route('/redflag/<int:redflagId>/comment', methods=['PATCH'])
def edit_redflag_comment(redflagId):
    # function for editing redflag comment
    if redflagId==0 or redflagId > len(redflags_list):
        return jsonify({"message": "Index is out of range"}), 400
    data=request.get_json()
    for incident in redflags_list:
        if int(incident.id)==int(redflagId):
            incident.comment=data['comment']
            return jsonify({
                "status": 200,
                "message": "incident updated"
                }), 200
        else:
         return jsonify({
             "error": "the redflag was not found",
             "status": 404
             }, 404)

@api.route('/redflag/<int:redflagId>', methods=['DELETE'])
def delete_redflag(redflagId):
    # deleting a redflag
    if redflagId==0 or redflagId > len(redflags_list):
        return jsonify({"message": "Index out of range"}), 400
    for incident in redflags_list:
        if incident.id==redflagId:
            redflags_list.remove(incident)
    return jsonify({
        "status": 200,
        "message": "redflag successfully deleted"
        }), 200
