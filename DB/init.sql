CREATE DATABASE students_db;
use students_db;
CREATE TABLE students (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(40) DEFAULT NULL,
  class int(11) DEFAULT NULL,
  gpa float DEFAULT NULL,
  sex varchar(5) DEFAULT NULL,
  age int(11) DEFAULT NULL,
  siblings int(11) DEFAULT NULL,
  uuid varchar(36) DEFAULT NULL,
  PRIMARY KEY (id)
) ;