'''
Created on 30-Jan-2020

@author: sneha
'''
import uuid
import logging
from Resources import db as connection
cursor = connection.cur


def savetodb(item):
    item["uuid"] = str(uuid.uuid4())
    logging.info("Saving Data given")
    query = """insert into {table}(name,class,sex,age,siblings,gpa,uuid) 
    values(%(name)s,%(class)s,%(sex)s,%(age)s,%(siblings)s,%(gpa)s,%(uuid)s)""".format(
        table="students")
    cursor.execute(query, item)
    return item


def getStudents():
    logging.info("Getting all Students")
    query = "select * from {table} ".format(
        table="students")
    cnt = cursor.execute(query)
    result = []
    headers = [list(i)[0] for i in cursor.description]
    for each in cursor.fetchall():
        s = dict(zip(headers, list(each)))
        result.append(s)
    return result


def getStudent(uuid):
    logging.info("Getting details of ",uuid)
    query = "select * from {table} where uuid =(%s)".format(
        table="students")
    cnt = cursor.execute(query, (uuid))
    res = {}
    if(cnt >= 1):
        headers = [list(i)[0] for i in cursor.description]
        row = cursor.fetchone()
        res = dict(zip(headers, list(row)))
    return res


def updateStudent(student, uuid):
    logging.info("Updating details of ",uuid)
    keylist = []
    for key in list(student):
        setquery = "{}=".format(key) + "%({})s".format(key)
        keylist.extend([setquery])
    vallist = ",".join(keylist)
    query = "update {table} set {values} where uuid= %(uuid)s;".format(
        table="students", values=vallist)
    student["uuid"] = uuid
    res = cursor.execute(query, student)
    logging.info("Updated Rows:", res)
    return res


def deleteStudent(uuid):
    logging.info("Deleting details of ",uuid)
    query = "delete from {table} where uuid =(%s)".format(
        table="students")
    res = cursor.execute(query, (uuid))
    logging.info("Deleted Rows :", res)
    return res
