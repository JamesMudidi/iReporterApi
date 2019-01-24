from flask import jsonify
from psycopg2.extras import RealDictCursor

from db.config import DatabaseConnection

conn = DatabaseConnection()


class Incident:
    # incident class
    def __init__(self, username, type, title, location,
                 status, Images, Videos, comment):
        self.createdBy = username
        self.type = type
        self.title = title
        self.location = location
        self.status = status
        self.Images = Images
        self.Videos = Videos
        self.comment = comment

    def create_incident(self):
        # creating an incident
        conn.cur.execute(
            "INSERT INTO incidents(createdBy, type, title, location, status, Images, Videos, comment) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                self.createdBy,
                self.type,
                self.title,
                self.location,
                self.status,
                self.Images,
                self.Videos,
                self.comment))
        conn.cur.execute("select * from incidents")
        incident = conn.cur.fetchall()[-1]

        print(incident)
        incident_type = ''

        if self.type == 'red-flag':
            incident_type = 'red-flag'
        else:
            incident_type = 'intervention'

        response = jsonify({
            "status": 201,
            "data": incident,
            "message": "Created " + incident_type + " record"
        }), 201

        return response
