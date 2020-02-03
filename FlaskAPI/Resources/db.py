'''
Created on 30-Jan-2020

@author: sneha
'''
import pymysql
dbconnection = pymysql.connect(
    host="mysql-server",
    db="students_db",
    user="root",
    password="root")
dbconnection.autocommit(True)
cur = dbconnection.cursor()

