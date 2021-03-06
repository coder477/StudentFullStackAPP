import React from 'react';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';

class AddEditForm extends React.Component {
  
  
  state = {
    uuid: '',
    name: '',
    clas: '',
    gpa: '',
    sex: '',
    age: '',
    siblings: ''
  }

  onChange = e => {
    this.setState({[e.target.name]: e.target.value})
  }

  submitFormAdd = e => {
    var POST_URL='http://localhost:5000/api/student';
    e.preventDefault()
    fetch(POST_URL, {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: this.state.name,
        class: this.state.clas,
        gpa: this.state.gpa,
        sex: this.state.sex,
        age: this.state.age,
        siblings: this.state.siblings
      })
    })
      .then(response => {
     	console.log(response)        
 		if (response.ok) {
         		return response.json();
       		} else {
          		throw new Error('Please check given input data');
       		}
     		})
      .then(student => {
          this.props.addStudentToState(student)
          this.props.toggle()
      })
      .catch(err => alert(err))
  }

  submitFormEdit = e => {
    var PUT_URL='http://localhost:5000/api/student/';
    e.preventDefault()
    fetch(PUT_URL+this.state.uuid, {
      method: 'put',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: this.state.name,
        class: this.state.clas,
        gpa: this.state.gpa,
        sex: this.state.sex,
        age: this.state.age,
        siblings: this.state.siblings
      })
    })
       .then(response => {
     	console.log(response)        
 		if (response.ok) {
         		return response.json();
       		} else {
          		throw new Error('Please check given input data');
       		}
     		})
      .then(student => {
        const clone = {...{
          uuid: this.state.uuid,
          name: this.state.name,
          class: this.state.clas,
          gpa: this.state.gpa,
          sex: this.state.sex,
          age: this.state.age,
          siblings: this.state.siblings
        }}
          this.props.updateState(clone)
          this.props.toggle()
      })
      .catch(err => alert(err))
  }

  componentDidMount(){
    // if student exists, populate the state with proper data
    if(this.props.student){
      const { uuid, name, clas, gpa, sex, age, siblings } = this.props.student
      this.setState({ uuid, name, clas, gpa, sex, age, siblings })
    }
  }

  render() {
    return (
      <Form onSubmit={this.props.student ? this.submitFormEdit : this.submitFormAdd}>
        <FormGroup>
          <Label for="name">name</Label>
          <Input type="text" name="name" id="name" onChange={this.onChange} value={this.state.name === null ? '' : this.state.name} />
        </FormGroup>
        <FormGroup>
          <Label for="clas">class</Label>
          <Input type="number" name="clas" id="clas" onChange={this.onChange} value={this.state.clas === null ? '' : this.state.clas}  />
        </FormGroup>
        <FormGroup>
          <Label for="gpa">gpa</Label>
          <Input type="number" name="gpa" id="gpa" onChange={this.onChange} value={this.state.gpa === null ? '' : this.state.gpa}  />
        </FormGroup>
        <FormGroup>
          <Label for="sex">sex</Label>
          <Input type="text" name="sex" id="sex" onChange={this.onChange} value={this.state.sex === null ? '' : this.state.sex} />
        </FormGroup>
        <FormGroup>
          <Label for="age">age</Label>
          <Input type="number" name="age" id="age" onChange={this.onChange} value={this.state.age === null ? '' : this.state.age} />
        </FormGroup>
        <FormGroup>
          <Label for="siblings">siblings</Label>
          <Input type="number" name="siblings" id="siblings" onChange={this.onChange} value={this.state.siblings}  />
        </FormGroup>
        <Button >Submit</Button>
      </Form>
    );
  }
}

export default AddEditForm
