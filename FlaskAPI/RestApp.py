'''
Created on 30-Jan-2020

@author: sneha
'''
from flask import Flask
from flask_restful import Api
from Resources import StudentApi
from Utils.Errors import errors
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}) # CORS setting up for all domains
api = Api(app, errors=errors)

"""Initialize API resources"""

api.add_resource(StudentApi.StudentsApi, '/api/students')
api.add_resource(StudentApi.StudentInsertionApi, '/api/student')
api.add_resource(StudentApi.StudentModificationApi, '/api/student/<uuid>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
    
