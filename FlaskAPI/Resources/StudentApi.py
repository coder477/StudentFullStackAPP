'''
Created on 30-Jan-2020

@author: sneha
'''
from flask import Response, request
from flask_restful import Resource
from Utils.Errors import *
from pymysql import err
from werkzeug import exceptions
from Resources import Service
from flask_restful.utils import cors
import json


class StudentsApi(Resource):
    @cors.crossdomain(origin='*')
    def get(self):
        try:
            students = Service.getStudents()
            return Response(json.dumps(students),
                             mimetype="application/json", status=200)
        except (exceptions.BadRequest, KeyError):
            raise BadRequestError
        except (err.InternalError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError


class StudentInsertionApi(Resource):
    @cors.crossdomain(origin='*')
    def post(self):
        try:
            req = request.get_json()
            student = Service.savetodb(req)
            return Response(json.dumps(student),
                            mimetype="application/json", status=200)
        except (exceptions.BadRequest, KeyError, TypeError):
            raise BadRequestError
        except (err.InternalError,err.DataError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError


class StudentModificationApi(Resource):
    @cors.crossdomain(origin='*')
    def put(self, uuid):
        try:
            student = request.get_json()
            result = Service.updateStudent(student, uuid)
            if(result > 0):
                return Response(json.dumps(''), mimetype="application/json", status=200)
            else:
                return Response(json.dumps('Given id does not exist.'),
                                mimetype="application/json", status=200)

        except exceptions.BadRequest:
            raise BadRequestError
        except err.ProgrammingError:
            raise SchemaValidationError
        except Exception:
            raise InternalServerError
        
        
    @cors.crossdomain(origin='*')
    def delete(self, uuid):
        try:
            result = Service.deleteStudent(uuid)
            headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": '*',
            "Access-Control-Allow-Methods": 'PUT, GET, POST, DELETE, OPTIONS',
            "Access-Control-Allow-Headers": 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            }
            if(result > 0):
                return Response(json.dumps(''), mimetype="application/json", headers=headers, status=204)
            else:
                return Response(json.dumps('Given id does not exist.'),
                                 mimetype="application/json",headers=headers, status=200)

        except Exception:
            raise InternalServerError
        
    @cors.crossdomain(origin='*')
    def get(self, uuid):
        try:
            res = Service.getStudent(uuid)
            return res
        except (TypeError):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError
