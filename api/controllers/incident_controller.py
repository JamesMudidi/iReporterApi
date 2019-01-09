'''
Import neccessary depencies
From the module or framework, we import the class datatype.
Using requst to add and access data
Using jsonify to generate JSON data
'''
from flask import jsonify, request, json
from api.models import incident_model
from api.validations import incident_validation

class Incident_controller:
    def add_incident(incidentType):
        data=request.get_json()

        incidentId=len(incidents_list)+1
        createdOn=datetime.datetime.now()
        createdBy=data.get('createdBy')
        incidentType=data.get('incidentType')
        location=geocoder.ip('me')
        status=data.get('status')
        images=data.get('images')
        videos=data.get('videos')
        comment=data.get('comment')

        if not createdBy:
            return jsonify({
                'status':400,
                'error':'createdBy has to be filled with string characters only'
                })
        if not images:
            return jsonify({
                'status':400,
                'error':'All incidents need to have images'
                })
        if not videos:
            return jsonify({
                'status':400,
                'error':'All incidents need to have videos'
                })
        if not comment:
            return jsonify({
                'status':400,
                'error':'comment has to be filled with string characters only'
                })

        if not validate_incident.validate_createdBy:
            return jsonify({
                'status':400,
                'error':'createdBy has to be filled with string characters only'
                })
        if not validate_incident.validate_images:
            return jsonify({
                'status':400,
                'error':'All incidents need to have images'
                })
        if not validate_incident.validate_videos:
            return jsonify({
                'status':400,
                'error':'All incidents need to have videos'
                })
        if not validate_incident.validate_comment:
            return jsonify({
                'status':400,
                'error':'comment has to be filled with string characters only'
                })

        if incidentType=='Redflag':
            incident=Incident(incidentId, createdOn, createdBy, incidentType,
            location, status, images, videos, comment)
        elif incidentType=='Intervention':
            incident=Incident(incidentId, createdOn, createdBy, incidentType,
            location, status, images, videos, comment)
        
        else:
            return jsonify({
                'error':'Invalid Incident type',
                'status':400
                }),400

    def get_all_incidents():
        if not Incident.incidents_list or len(Incident.incidents_list) <= 0 :
            return jsonify({
                'status':400,
                'error':'No incidents found in system'
            }),400
        return jsonify({
            'status':200,
            'data':incidents_list,
            'message':'Here is a list of all the incidents'
            })

    def get_all_redflags():
      for Redflag in Incident.incidents_list:
        if Redflag['incidentType'] == Redflag:
            return jsonify({
                'status':200,
                'data':Redflag
                }),200
        return jsonify({
            'status':200,
            'message':'No Redflags in the system yet'})

    def get_all_interventions():
      for Intervention in Incident.incidents_list:
        if Intervention['incidentType'] == Intervention:
            return jsonify({
                'status':200,
                'data':Intervention
                }),200
        return jsonify({
            'status':200,
            'message':'No Interventions in the system yet'
            }), 200

    def get_a_redflag(incidentId):
      for Redflag in Incident.incidents_list:
        if Redflag['incidentId'] == incidentId and Redflag['incidentType'] == Redflag:
            return jsonify({
                'status':200,
                'data':Redflag
                }),200
        return jsonify({
            'status':200,
            'message':'Invalid ID or Redflag not in the system'})

    def get_an_intervention(incidentId):
      for Intervention in Incident.incidents_list:
        if Intervention['incidentId'] == incidentId and Intervention['incidentType'] == Intervention:
            return jsonify({
                'status':200,
                'data':Intervention
                }),200
        return jsonify({
            'status':200,
            'message':'Invalid ID or Intervention not in the system'
            }), 200

    def edit_redflag_location(incidentId):
      request_data = request.get_json()
      location = request_data.get('location')
      for redflag in Incident.incidents_list:
        if redflag['incidentId'] == incidentId:
            new_location = location
            redflag['location'] = new_location
            return jsonify({
                'status':200,
                'data':Redflag,
                'message': 'Redflag location has been updated'
                }),200
      return jsonify({
        'status':200,
        'data':Redflag,
        'message':'Redflag location could not be updated'
        }),400

    def edit_intervention_location(incidentId):
      request_data = request.get_json()
      location = request_data.get('location')
      for intervention in Incident.incidents_list:
        if intervention['incidentId'] == incidentId:
            new_location = location
            intervention['location'] = new_location
            return jsonify({
                'status':200,
                'data':Intervention,
                'message': 'Intervention location has been updated'
                }),200
      return jsonify({
        'status':200,
        'data':Intervention,
        'message':'Intervention location could not be updated'
        }),400

    def edit_redflag_comment(incidentId):
      request_data = request.get_json()
      comment = request_data.get('comment')
      for redflag in Incident.incidents_list:
        if redflag['incidentId'] == incidentId:
            new_comment = comment
            redflag['comment'] = new_comment
            return jsonify({
                'status':200,
                'data':Redflag,
                'message': 'Redflag Comment has been updated'
                }),200
      return jsonify({
        'status':200,
        'data':Redflag,
        'message':'Redflag Comment could not be updated'
        }),400

    def edit_intervention_comment(incidentId):
      request_data = request.get_json()
      comment = request_data.get('comment')
      for intervention in Incident.incidents_list:
        if intervention['incidentId'] == incidentId:
            new_comment = comment
            intervention['comment'] = new_comment
            return jsonify({
                'status':200,
                'data':Intervention,
                'message': 'Intervention Comment has been updated'
                }),200
      return jsonify({
        'status':200,
        'data':Intervention,
        'message':'Intervention Comment could not be updated'
        }),400

    def edit_redflag_status(incidentId):
      request_data = request.get_json()
      status = request_data.get('status')
      for redflag in Incident.incidents_list:
        if redflag['incidentId'] == incidentId:
            new_status = status
            redflag['status'] = new_status
            return jsonify({
                'status':200,
                'data':Redflag,
                'message': 'Redflag Status has been updated'
                }),200
      return jsonify({
        'status':200,
        'data':Redflag,
        'message':'Redflag Status could not be updated'
        }),400

    def edit_intervention_status(incidentId):
      request_data = request.get_json()
      status = request_data.get('status')
      for intervention in Incident.incidents_list:
        if intervention['incidentId'] == incidentId:
            new_status = status
            intervention['status'] = new_status
            return jsonify({
                'status':200,
                'data':Intervention,
                'message': 'Intervention Status has been updated'
                }),200
      return jsonify({
        'status':200,
        'data':Intervention,
        'message':'Intervention Status could not be updated'
        }),400

def delete_redflag(incidentId): 
    for redflag in Incident.incidents_list:
        if redflag['incidentId']==incidentId:
            if len(incidents)==0:
                return jsonify({
                    'status':400,
                    'data':incidents,
                    'message':'Invalid ID or Redflag not in the system'
                    }),400
        Incidents.incidents_list.pop(redflag[0])
        return jsonify({
            'status': 200,
            'data':incidents,
            'message':'Incident has been deleted'})

def delete_intervention(incidentId): 
    for intervention in Incident.incidents_list:
        if intervention['incidentId']==incidentId:
            if len(incidents)==0:
                return jsonify({
                    'status':400,
                    'data':incidents,
                    'message':'Invalid ID or Intervention not in the system'
                    }),400
        Incidents.incidents_list.pop(intervention[0])
        return jsonify({
            'status': 200,
            'data':incidents,
            'message':'Incident has been deleted'})