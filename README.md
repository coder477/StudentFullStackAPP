# StudentFullStackAPP

### Prerequisites
* Docker

### Running the application:
```sh
$ docker-compose up // from application's location (takes little time to set up react app for the first time due to nodejs setup)
``` 
* From browser run the following to interact with APIs through React user interface.

` http://localhost:3000 `
 
* Testing APIs without UI from Terminal/POSTMAN


  Insert a student data
  
  `curl -X POST   http://localhost:5000/api/student   -H 'content-type: application/json'   -d '{"class": 3, "name":"Steve Jones",    "sex":    "male",    "age": 22,    "siblings":    1,"gpa":7.25}'` 
  
  Get all students Data
 
  `curl -X GET 'http://localhost:5000/api/students'`
  
  Get a student data
  
  `curl -X GET 'http://localhost:50000/api/student/<uuid>'`
  
  Update a student data
  
  `curl -X PUT   http://localhost:5000/api/student/<uuid>   -H 'content-type: application/json'   -d '{"class": 3,   "name":"newname",  "sex": "male",  "age":10,  "siblings":  1,"gpa":7.25}'`
  
  Delete a student data
  
  `curl -X DELETE 'http://localhost:50000/api/student/<uuid>'`
  
### Python Modules Used : all modules are mentioned in requiements.txt 
* flask-restful for API
* flask-cors for handling CORS issues
* pymysql for MySQL connection

### Improvements:
* Unit Tests can be added (Added only Integration testing in the application here)
* React App is a simple application and interface and validations can be improved. 

