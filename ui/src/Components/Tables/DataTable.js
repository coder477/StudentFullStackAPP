import React, { Component } from 'react'
import { Table, Button } from 'reactstrap';
import ModalForm from '../Modals/Modal'

class DataTable extends Component {

  deleteStudent = id => {
    let confirmDelete = window.confirm('Delete student forever?')
    if(confirmDelete){
      fetch('http://localhost:5000/api/student/'+id, {
      method: 'delete',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => console.log(response))
      .then(student => {
        this.props.deleteStudentFromState(id)
      })
      .catch(err => alert(err))
    }

  }

  render() {


    const students = this.props.students.map(student => {
      return (
        <tr key={student.uuid}>
          <th scope="row">{student.uuid}</th>
          <td>{student.class}</td>
          <td>{student.gpa}</td>
          <td>{student.sex}</td>
          <td>{student.age}</td>
          <td>{student.siblings}</td>
          <td>
            <div style={{width:"110px"}}>
              <ModalForm buttonLabel="UPDATE" student={student} updateState={this.props.updateState}/>
              {' '}
              <Button color="danger" onClick={() => this.deleteStudent(student.uuid)}>DELETE</Button>
            </div>
          </td>
        </tr>
        )
      })

    return (
      <Table responsive hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Class</th>
            <th>GPA</th>
            <th>Sex</th>
            <th>Age</th>
            <th>Siblings</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {students}
        </tbody>
      </Table>
    )
  }
}

export default DataTable