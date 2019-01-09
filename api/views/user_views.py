from flask import Flask, jsonify, request, json
from api import app
from api.controllers.users_controllers import UsersController

users_controller = UsersController()

@app.route('/')
def index():
    return jsonify({
        "Application":"iReporter"
        },
        {
        "Create RedFlag": "/api/v1/red-flags",
        "View all RedFlags": "/api/v1/red-flags",
        "View single RedFlag": "/api/v1/red-flags/<int:_id",
        "Patch RedFlag comment": "/api/v1/red-flags/<int:_id>/comment",
        "Patch RedFlag location": "/api/v1/red-flags/<int:_id>/location",
        "Delete RedFlag": "api/v1/red-flag/<int:_id>"
    })

@app.route('/api/v1/users', methods=['POST'])
def register_user():
    request_data = request.get_json()
    return users_controller.add_user(request_data) 
