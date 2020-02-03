'''
Created on 30-Jan-2020

@author: sneha
'''
import uuid
from Resources import db as connection
cursor = connection.cur


def savetodb(item):
    item["uuid"] = str(uuid.uuid4())
    print("saving data")
    query = """insert into {table}(name,class,sex,age,siblings,gpa,uuid) 
    values(%(name)s,%(class)s,%(sex)s,%(age)s,%(siblings)s,%(gpa)s,%(uuid)s)""".format(
        table="students")
    res = cursor.execute(query, item)
    print(res, "resss", item["uuid"])
    return item["uuid"]


def getStudents():
    print("get all students")
    query = "select * from {table} ".format(
        table="students")
    cnt = cursor.execute(query)
    print("getting items ", cnt)
    result = []
    headers = [list(i)[0] for i in cursor.description]
    for each in cursor.fetchall():
        s = dict(zip(headers, list(each)))
        result.append(s)
    return result


def getStudent(uuid):
    print("get given students")
    query = "select * from {table} where uuid =(%s)".format(
        table="students")
    cnt = cursor.execute(query, (uuid))
    res = {}
    if(cnt >= 1):
        print("getting item ", cnt)
        headers = [list(i)[0] for i in cursor.description]
        row = cursor.fetchone()
        print(row)
        res = dict(zip(headers, list(row)))
        print(res)
    return res


def updateStudent(student, uuid):
    print("update given student")
    keylist = []
    for key in list(student):
        setquery = "{}=".format(key) + "%({})s".format(key)
        keylist.extend([setquery])
    vallist = ",".join(keylist)
    query = "update {table} set {values} where uuid= %(uuid)s;".format(
        table="students", values=vallist)
    print(query)
    student["uuid"] = uuid
    res = cursor.execute(query, student)
    print("ress", res)
    return res


def deleteStudent(uuid):
    print("delete given student")
    query = "delete from {table} where uuid =(%s)".format(
        table="students")
    res = cursor.execute(query, (uuid))
    print("ress", res)
    return res
