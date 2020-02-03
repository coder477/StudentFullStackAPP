'''
Created on 02-Feb-2020

@author: sneha
'''
from copy import deepcopy
import unittest
from unittest import TestCase
import json
from RestApp import app



class Test(TestCase):

    def setUp(self):
        self.STUDENTS_URL = 'http://localhost:5000/api/students'
        self.STUDENT_ERROR_URL = 'http://localhost:5000/api/student/a561dbf7-d0ed-404c-ad7e-46c10f9271'
        self.POST_STUDENT_URL = 'http://localhost:5000/api/student'
        self.STUDENT_URL='http://localhost:5000/api/student/'
        self.app = app.test_client()
        self.app.testing = True
        
        
    def test1_end_to_end_flow_without_errors(self):
        """insert a student data"""
        student = {
        "id": 12,
        "name": "Name1",
        "class": 3,
        "gpa": 7.25,
        "sex": "male",
        "age": 10,
        "siblings": 1,
        }
        response = self.app.post(self.POST_STUDENT_URL,
                                data=json.dumps(student),
                                content_type='application/json')
        student = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        student_id=student['uuid']
        self.STUDENT_URL=self.STUDENT_URL+student_id
        
        """Getting the inserted student details"""
        
        response = self.app.get(self.STUDENT_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        
        """insert a second student data"""
        
        student = {
        "id": 12,
        "name": "Name2",
        "class": 4,
        "gpa": 7.25,
        "sex": "male",
        "age": 10,
        "siblings": 1,
        }
        response = self.app.post(self.POST_STUDENT_URL,
                                data=json.dumps(student),
                                content_type='application/json')
        student = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        
        """get the two students data"""
        
        response = self.app.get(self.STUDENTS_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        
        """update the student1's data"""
        
        student = {
        "id": 12,
        "name": "sneha",
        "class": 3,
        "gpa": 7.25,
        "sex": "male",
        "age": 10,
        "siblings": 1,
        }
        response = self.app.put(self.STUDENT_URL,
                                data=json.dumps(student),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        """delete student1's data"""
        
        response = self.app.delete(self.STUDENT_URL)
        self.assertEqual(response.status_code, 204)



    """testing error results of all methods"""   
        
    def test2_post_student_with_bad_request(self):
        student = {
        "id": 12,
        "class": 3,
        "gpa": 7.25,
        "sex": "male",
        "age": 10,
        "siblings": 1,
        }
        response = self.app.post(self.POST_STUDENT_URL,
                                data=json.dumps(student),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)

        
    def test3_get_student_does_not_exist(self):
        response = self.app.get(self.STUDENT_ERROR_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 0)

        
    def test4_update_student_does_not_exist(self):
        student = {
        "id": 12,
        "name": "sneha",
        "class": 3,
        "gpa": 7.25,
        "sex": "male",
        "age": 10,
        "siblings": 1,
        }
        response = self.app.put(self.STUDENT_ERROR_URL,
                                data=json.dumps(student),
                                content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, 'Given id does not exist.')



    def test5_delete_student_does_not_exist(self):
        response = self.app.delete(self.STUDENT_ERROR_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, 'Given id does not exist.')




if __name__ == "__main__":
    unittest.main()
