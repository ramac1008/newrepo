#!/usr/bin/python
# -*- utf-8 -*-
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import psycopg2

app = Flask(__name__)
api = Api(app)

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="R0ck3tD0ct0r",
    host="172.17.48.3",
    port="5432"
)


class Users(Resource):
    def get(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM appointments ")
        rows = cur.fetchall()
        cur.close()
        users = []
        for row in rows:
            users.append({
                "id": row[0],
                "patient_id": row[1],
                "user_id": row[2],
                "date_time": row[4]
            })
        return jsonify(users)


api.add_resource(Users, "/users")


class Patients(Resource):
    def get(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM patients")
        rows = cur.fetchall()
        cur.close()
        patients = []
        for row in rows:
            patients.append({
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "phone_number": row[3]
            })
        return jsonify(patients)


api.add_resource(Patients, "/patients")


class Root(Resource):
    def get(self):
        response = {'message': 'Welcome to the API'}
        return jsonify(response)


api.add_resource(Root, "/")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
