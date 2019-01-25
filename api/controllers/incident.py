from flask import Flask, jsonify, request
from marshmallow import ValidationError, Schema, fields
from psycopg2.extras import RealDictCursor
import datetime
import smtplib

from api import app
from api.controllers import Incident
from api.common.validator import email, required, verifyStatus, verifyType
from api.views import api
from api.common.authenticator import authenticate
from db.config import DatabaseConnection
from api.views.errors import error_response

class incident:
	def create_incident(identity, data, type):
    createdBy = identity
    status = 'draft'
    incident = Incident(createdBy['id'], type, data['title'], data['location'],
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


def edit_incident(update_type, incident_id, update_record, type, indentity):
    # function for editing incidents
    conn.cur.execute(
        "select * from incidents where id = '{}' and type = '{}'".format(incident_id, type))
    incident = conn.cur.fetchone()

    if incident is None:
        return jsonify({
            "status": 404,
            "message": "The " + type + " record was not found"
        }), 404

    if verified(indentity):
        query = "update incidents set " + update_type + \
            " = '{}' where id = '{}'".format(update_record, incident_id)
        conn.cur.execute(query)
        if update_type == 'status':
            sendEmail(indentity, type, update_record)
        return jsonify({"status": 200, "message": "Updated " +
                        incident['type'] + " record's " + update_type}), 200
    else:
        return error_response(
            403, "You do not have permissions to access this record")


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
    cconn.cur.commit()
    return jsonify({
        "message": type + " record was deleted"
    }), 200


def isAdmin(user_id):
    conn.cur.execute("SELECT * from users WHERE id='{}'".format(user_id['id']))
    user = conn.cur.fetchone()
    return user['isadmin']


def verified(user_id,):
    conn.cur.execute("select * from incidents where type='{}'".format(user_id['id']))
    incident = conn.cur.fetchone()
    if incident is None and isAdmin(user_id) == False:
        return False
    return True


def sendEmail(user_id, incident_type, status):
    conn.cur.execute("select * from users where id = '{}'".format(user_id))
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


