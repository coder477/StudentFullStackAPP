import React, { Component } from 'react'
import { Container, Row, Col } from 'reactstrap'
import ModalForm from './Components/Modals/Modal'
import DataTable from './Components/Tables/DataTable'
import { Button } from 'reactstrap';


class App extends Component {
  
  state = {
    students: []
  }

  getStudents(){
  var GET_URL='http://localhost:5000/api/students';
    fetch(GET_URL)
      .then(response => response.json())
      .then(students => this.setState({students}))
      .catch(err => alert(err))
  }

  addStudentToState = (student) => {
    this.setState(prevState => ({
      students: [...prevState.students, student]
    }))
  }

  updateState = (student) => {
    const studentIndex = this.state.students.findIndex(data => data.uuid === student.uuid)
    const newArray = [
      ...this.state.students.slice(0, studentIndex),
      student,
      ...this.state.students.slice(studentIndex + 1)
    ]
    this.setState({ students: newArray })
  }

  deleteStudentFromState = (id) => {
    const updatedStudents = this.state.students.filter(student => student.uuid !== id)
    this.setState({ students: updatedStudents })
  }

  componentDidMount(){
    this.getStudents()
  }

  render() {
    return (
      <Container className="App">
        <Row>
          <Col>
            <h1 style={{margin: "20px 0"}}>Student Data Application</h1>
            <h5>** Add data for testing API services</h5>
          </Col>
        </Row>
        <Row>
          <Col>
            <DataTable students={this.state.students} updateState={this.updateState} deleteStudentFromState={this.deleteStudentFromState} />
          </Col>
        </Row>
        <Row>
          <Col>
            <Button color="primary"  style={{float: "left", marginRight: "10px"}} onClick={this.getStudents.bind(this)}>Refresh Students</Button>
            <ModalForm buttonLabel="Add Student" addStudentToState={this.addStudentToState}/>
          </Col>
        </Row>
      </Container>
    )
  }
}

export default App
