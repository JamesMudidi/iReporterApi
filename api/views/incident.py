from flask import Flask, jsonify, request
from marshmallow import ValidationError, Schema, fields
from psycopg2.extras import RealDictCursor
import datetime
import smtplib

from api import app
from api.models.incident import Incident
from api.models.incident import Incident
from api.common.validator import email, required, verifyStatus, verifyType
from api.views import api
from api.common.authenticator import authenticate
from db.config import DatabaseConnection
from api.views.errors import error_response

email = "mudidi.jimmy@gmail.com"
password = "postgres"
conn = DatabaseConnection()

class IncidentSchema(Schema):
    # Represents the schema for incidents
    type = fields.Str(required=False)
    title = fields.Str(required=True, validate=(required))
    comment = fields.Str(required=True, validate=(required))
    location = fields.Str(required=True, validate=(required))
    id = fields.Int(required=False)
    createdOn = fields.Str(required=False)
    createdBy = fields.Str(required=False)
    Images = fields.Str(required=False)
    status = fields.Str(required=False)
    Videos = fields.Str(required=False)


class IncidentStatusSchema(Schema):
    # Represents the schema for incidents status edit
    type = fields.Str(required=True, validate=(verifyType))
    title = fields.Str(required=True, validate=(required))
    comment = fields.Str(required=True, validate=(required))
    location = fields.Str(required=True, validate=(required))
    id = fields.Int(required=False)
    createdOn = fields.Str(required=False)
    createdBy = fields.Int(required=False)
    Images = fields.Str(required=False)
    status = fields.Str(required=True, validate=(verifyStatus))
    Videos = fields.Str(required=False)


@api.route('/redflags', methods=['POST'])
@authenticate
def create_redflag(identity):
    if isAdmin(identity):
        return error_response(
            403, "Administrator cannot create an incident record")
    else:
        data=request.get_json('data')
        data, errors = IncidentSchema().load(data)
        if errors:
            return jsonify({
                "errors": errors,
                "status": 400}), 400
        return incident.create_incident(identity, data, 'redflag')


@api.route('/interventions', methods=['POST'])
@authenticate
def create_intervention(identity):
    if isAdmin(identity):
            return error_response(
        403, "Administrator cannot create an incident record")
    else:
        data=request.get_json('data')
        data, errors = IncidentSchema().load(data)
        if errors:
            return jsonify({
                "errors": errors,
                "status": 400}), 400
        return incident.create_incident(identity, data, 'intervention')


@api.route('/interventions', methods=['GET'])
@authenticate
def get_interventions(identity):
    # getting all interventions
    return get_incidents('intervention', identity)


@api.route('/redflags', methods=['GET'])
@authenticate
def get_redflags(identity):
    # getting all redflags
    return get_incidents('redflag', identity)


@api.route('/incidents', methods=['GET'])
@authenticate
def get_all(identity):
    # getting all incidents
    return get_all_incidents(identity, type)


@api.route('/redflags/<int:redflag_id>', methods=['GET'])
@authenticate
def get_single_redflag(identity, redflag_id):
    # getting a single redflag
    if verified(identity):
        return error_response(
            403, "You do not have permissions to access this record")
    else:
        return get_single_incident(redflag_id, 'redflag')


@api.route('/interventions/<int:intervention_id>', methods=['GET'])
@authenticate
def get_single_intervention(identity, intervention_id):
    # getting a intervention redflag
    if verified(identity):
        return error_response(
            403, "You do not have permissions to access this record")
    else:
        return get_single_incident(intervention_id, 'intervention')


@api.route('/redflags/<int:redflag_id>/status', methods=['PATCH'])
@authenticate
def edit_redflag_status(identity, redflag_id):
    # editing status of a redflag record

    if isAdmin(identity):
        return error_response(
            403, "You do not have permissions to access this record")
    else:
        data, errors = IncidentStatusSchema().load(request.get_json())

        if errors:
            return jsonify({
                "errors": errors,
                "status": 400}), 400

        if data['type'] == 'intervention':
            return jsonify({
                "errors": "This edits the redflag status only",
                "status": 400}), 400

        if not data['status'].strip(' '):
            return jsonify({
                "errors": "Redflag status cannot be empty",
                "status": 400}), 400

        return edit_incident(
            'status',
            redflag_id,
            data['status'],
            'redflag',
            identity)


@api.route('/interventions/<int:intervention_id>/status', methods=['PATCH'])
@authenticate
def edit_intervention_status(identity, intervention_id):
    # editing status of an intervention record

    if isAdmin(identity):
        return error_response(
            403, "You do not have permissions to access this record")
    else:
        data, errors = IncidentStatusSchema().load(request.get_json())
        if errors:
            return jsonify({
                "errors": errors,
                "status": 400}), 400

        if data['type'] == 'redflag':
            return jsonify({
                "errors": "This edits the intervention stutus only",
                "status": 400}), 400

        if not data['status'].strip(' '):
            return jsonify({
                "errors": "Intervention status cannot be empty",
                "status": 400}), 400

        return edit_incident(
            'status',
            intervention_id,
            data['status'],
            'intervention',
            identity)


@api.route('/redflags/<int:redflag_id>/location', methods=['PATCH'])
@authenticate
def edit_redflag_location(identity, redflag_id):
    # editing location of a redflag record
    data, errors = IncidentSchema().load(request.get_json())

    if errors:
        return jsonify({
            "errors": errors,
            "status": 400}), 400

    if not data['type'].strip(' '):
        return jsonify({
            "errors": "type cannot be empty",
            "status": 400}), 400

    if data['type'] == 'intervention':
        return jsonify({
            "errors": "This edits the Redflag location only",
            "status": 400}), 400

    return edit_incident(
        'location',
        redflag_id,
        data['location'],
        'redflag',
        identity)


@api.route('/interventions/<int:intervention_id>/location', methods=['PATCH'])
@authenticate
def edit_intervention_location(identity, intervention_id):
    # editing status of an intervention record
    data, errors = IncidentSchema().load(request.get_json())

    if errors:
        return jsonify({
            "errors": errors,
            "status": 400}), 400

    if not data['type'].strip(' '):
        return jsonify({
            "errors": "type cannot be empty",
            "status": 400}), 400

    if data['type'] == 'redflag':
        return jsonify({
            "errors": "This edits the Intervention record only",
            "status": 400}), 400

    return edit_incident(
        'location',
        intervention_id,
        data['location'],
        'intervention',
        identity)


@api.route('/interventions/<int:intervention_id>/comment', methods=['PATCH'])
@authenticate
def edit_intervention_comment(identity, intervention_id):
    # editing status of an intervention record
    data, errors = IncidentSchema().load(request.get_json())

    if errors:
        return jsonify({
            "errors": errors,
            "status": 400}), 400

    if data['type'] == 'redflag':
        return jsonify({
            "errors": "This edits the Intervention comment only",
            "status": 400}), 400

    return edit_incident(
        'comment',
        intervention_id,
        data['comment'],
        'intervention',
        identity)


@api.route('/redflags/<int:redflag_id>/comment', methods=['PATCH'])
@authenticate
def edit_redflag_comment(identity, redflag_id):
    # editing status of a redflag record
    data, errors = IncidentSchema().load(request.get_json())

    if errors:
        return jsonify({
            "errors": errors,
            "status": 400}), 400

    if data['type'] == 'intervention':
        return jsonify({
            "errors": "This edits the Redflag comment only",
            "status": 400}), 400

    return edit_incident(
        'comment',
        redflag_id,
        data['comment'],
        'redflag',
        identity)


@api.route('/redflags/<int:redflags_id>', methods=['DELETE'])
@authenticate
def delete_redflag(identity, redflags_id):
    # deleting a redflag record
    if verified(identity):
        return error_response(
            403, "You do not have permissions to access this record")
    else:
        return delete_incident(redflags_id, 'redflag')


@api.route('/interventions/<int:intervention_id>', methods=['DELETE'])
@authenticate
def delete_intervention(identity, intervention_id):
    # deleting an intervention record
    if verified(identity):
        return error_response(
            403, "You do not have permissions to access this record")
    else:
        return delete_incident(intervention_id, 'intervention')


@api.route('/incidents/<int:incident_id>', methods=['PATCH'])
@authenticate
def edit_any_incident(indentity, incident_id):

    # function for editing incidents
    data, errors = IncidentSchema().load(request.get_json())

    location = data['location']
    comment = data['comment']

    conn.cur.execute(
        "select * from incidents where id = '{}'".format(incident_id))
    incident = conn.cur.fetchone()

    if incident is None:
        return jsonify({
            "status": 404,
            "message": "The record was not found"
        }), 404

    if verified(indentity):
        return error_response(
            403, "You do not have permissions to access this record")
    else:
        query = "update incidents set location = '{}', comment = '{}' where id = '{}'".format(
            location, comment, incident_id)
        conn.cur.execute(query)
        return jsonify(
            {"status": 200, "message": "Record successfully updated"}), 200


class incident:
    def create_incident(identity, data, type):
        createdBy = identity
        createdon = 'today'
        status = 'Draft'
        incident = Incident(createdBy['id'], createdon, type, data['title'], data['location'],
                            status, data['Images'], data['Videos'], data['comment'])
        response = incident.create_incident()
        return response


def get_incidents(type, identity):
    incidents = ()

    if isAdmin(identity):
        conn.cur.execute("select * from incidents where type = '{}'".format(type))
        incidents = conn.cur.fetchall()
    else:
        conn.cur.execute(
            "select * from incidents where type = '{}'".format(type))
        incidents = conn.cur.fetchall()

    if not incidents:
        return jsonify({
            "status": 404,
            "message": "There are no " + type + "s"
        }), 404

    return jsonify({
        "status": 200,
        "data": incidents
    }), 200


def get_all_incidents(identity, type):
    incidents = ()

    if not isAdmin(identity):
        conn.cur.execute("select * from incidents")
        incidents = conn.cur.fetchall()
    else:
        conn.cur.execute("select * from incidents")
        incidents = conn.cur.fetchall()

    if not incidents:
        return jsonify({
            "status": 404,
            "message": "There are no " + type + "s"
        }), 404
    return jsonify({
        "status": 200,
        "data": incidents
    }), 200


def get_single_incident(incident_id, type):
    conn.cur.execute(
        "select * from incidents where id = '{}' and type = '{}'".format(incident_id, type))
    incident = conn.cur.fetchone()

    if incident is None:
        return jsonify({
            "status": 404,
            "message": "The " + type + " record was not found"
        }), 404

    return jsonify({
        "status": 200,
        "data": incident
    }), 200


def edit_incident(update_type, incident_id, update_record, type, indentity):
    # function for editing incidents
    conn.cur.execute(
        "select * from incidents where id = '{}' and type = '{}'".format(incident_id, type))
    incident = conn.cur.fetchone()

    if incident is None:
        return jsonify({
            "status": 404,
            "message": "The " + type + " incident was not found"
        }), 404

    if verified(indentity):
        return error_response(
            403, "You do not have permissions to access this record")
    else:
        query = "update incidents set " + update_type + \
            " = '{}' where id = '{}'".format(update_record, incident_id)
        conn.cur.execute(query)
        if update_type == 'status':
            sendEmail(indentity, type, update_record)
        return jsonify({"status": 200, "message": "Updated " +
                        incident['type'] + " record's " + update_type}), 200


def delete_incident(incident_id, type):
    conn.cur.execute(
        "select * from incidents where id = '{}' and type = '{}'".format(incident_id, type))
    incident = conn.cur.fetchone()

    if not incident:
        return jsonify({
            "status": 404,
            "message": "The " + type + " record was not found"
        }), 404

    conn.cur.execute("delete from incidents where id = '{}'".format(incident_id))
    return jsonify({
        "message": type + " incident was deleted successfully"
    }), 200


def isAdmin(user_id):
    conn.cur.execute("SELECT * from users WHERE id='{}'".format(user_id['id']))
    user = conn.cur.fetchone()
    return user['isadmin']


def verified(createdBy):
    conn.cur.execute("select * from incidents where type='{}'".format(createdBy['id']))
    incident = conn.cur.fetchone()
    if incident is None:
        return False
    return True


def sendEmail(user_id, incident_type, status):
    conn.cur.execute("select * from users where id = '{}'".format(user_id['id']))
    user = conn.cur.fetchone()
    FROM = email
    TO = user['email']
    SUBJECT = "iReporter Status Changed"
    TEXT = "Your " + incident_type + " status has changed to " + status

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(email, password)
        smtpserver.sendmail(FROM, TO, message)
        smtpserver.close()
        print('email successfully sent')
    except BaseException:
        print('email failed to send')


@app.errorhandler(404)
def not_found(error):
    '''404 Error function'''
    return (jsonify(
        {'error': 'We could not find what you are looking for.'}), 404)


@app.errorhandler(400)
def bad_request(error):
    '''400 Error function'''
    return (jsonify(
        {'error': 'Error in the data formart. The Kind of data you are posting is not the required type'}), 400)


@app.errorhandler(405)
def method_not_allowed(error):
    return (jsonify(
        {'error': 'The method provided is not allowed for the endpoint used.'}), 405)


@app.errorhandler(500)
def server_error(error):
    return (
        jsonify({'error': 'Oops! Something happened :( Internal server error.'}), 500)
