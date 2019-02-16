from flask import jsonify


def error_response(status_code, msg):
    response = jsonify({
        'status': status_code,
        'message': msg
    })
    response.status_code = status_code
    return response