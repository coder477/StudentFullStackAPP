'''
Created on 02-Feb-2020

@author: sneha
'''

class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class StudentAlreadyExistsError(Exception):
    pass


class UpdatingStudentError(Exception):
    pass


class DeletingStudentError(Exception):
    pass


class BadRequestError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Given input fields has incorrect data . Please check",
        "status": 400
    },

    "StudentAlreadyExistsError": {
        "message": "Student with given name already exists",
        "status": 400
    },
    "UpdatingStudentError": {
        "message": "Some issue in Updating student",
        "status": 400
    },
    "DeletingStudentError": {
        "message": "Some issue Deleting student",
        "status": 400
    },
    "BadRequestError": {
        "message": "Bad Request Received. Please check the given input",
        "status": 400
    },


}
