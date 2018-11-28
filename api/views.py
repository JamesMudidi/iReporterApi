from flask import Flask, jsonify, request
from api.models.models import User
from api.models.user_list import UserList
from api.models.incedent_list import Incident

app = Flask(__name__)

user = UserList()
incedent = Incident()

@app.route('/')
def index():
    return jsonify({"message": "Welcome to iReporter"})


@app.route('/api/v1/users', methods=['POST'])
def registre_user():
    data = request.get_json()
    id = 1
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othername = data.get('othername')
    email = data.get('email')
    phone_number = data.get('phone_number')
    username = data.get('username')
    registered = data.get('date')
    is_admin = data.get('is_admin')

    user.add_new_user(id,firstname,lastname,othername,email,
                            phone_number,username,registered,is_admin)
    return jsonify({"message": "user registerd"}), 201
    

@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    users = user.retreave_users()

  
    return jsonify({"users":users}), 200 


@app.route('/api/v1/red-flag', methods=['POST'])
def create_incident():
    data = request.get_json()
    incident_id=1
    created_on = data.get('created_on')
    type = data.get('type')
    location = data.get('location')
    status = data.get('status')
    image = data.get('image')
    videos = data.get('videos')
    comment = data.get('comment')

    incedent.create_incedent(incident_id, created_on, type,
                            location, status, image,videos,
                            comment)
    return jsonify({"message":"Incident Created Successfully","status": 201}), 201



@app.route('/api/v1/red-flag', methods=['GET'])
def all_incidents():
    incidents = incedent.retreave_all_incidents()
    return jsonify({"incidents":incidents,"message":"sucessful"}), 200



@app.route('/api/v1/red-flag/<int:incedentid>',methods=['GET'])
def specific_incident(incedentid):
   
    incedents = Incident()
    red_flag = incedents.retreave_all_incidents()
    for incedent in red_flag:
        if incedent.get('incident_id') == incedentid:
            return jsonify({"message":"all the incedents","incedent":incedent}), 200
    return jsonify({"message":"Incedent not found"}), 200


# @app.route('/api/v1/red-flag/<int:incedentid>/comment', methods=['PATCH'])
# def patch_comment_specific_incident(incedentid):
#     incedents = Incident()
#     red_flag = incedents.retreave_all_incidents()
#     for incedent in red_flag:
#         if incedent['incident_id'] == incedentid:
#             return jsonify({"message": "all the incedents", "incedent": incedent}), 200
#     return jsonify({"message": "Incedent not found", "incedent": incedents}), 200


# @app.route('/api/v1/red-flag/<int:incedentid>/location', methods=['PATCH']) 
# def patch_location_specific_incident(incedentid):
#     incedents = Incident()
#     red_flag = incedents.retreave_all_incidents()
#     for incedent in red_flag:
#         if incedent['incident_id'] == incedentid:
#             return jsonify({"message": "all the incedents", "incedent": incedent}), 200
#     return jsonify({"message": "Incedent not found", "incedent": incedents}), 200


# @app.route('/api/v1/red-flag/<int:incedentid>', methods=['DELETE'])
# def delete_specific_incident(incedentid):
#     incedents = Incident()
#     red_flag = incedents.retreave_all_incidents()
#     for incedent in red_flag:
#         if incedent['incident_id'] == incedentid:
#             del(self.incident_list)
#     return jsonify({"message": "Incedent not found", "incedent": incedents}), 200






