import React from 'react'
import styled from 'styled-components'
import axios from 'axios';

function Settings() {
  const handleOnsubmit = async (e) => {
    e.preventDefault();
    console.log(e.target)
    const name = e.target.name.value;
    const email = e.target.email.value;
    const password = e.target.password.value;

    const data = {
      "name": name,
      "email": email,
      "password": password,
    };

    try {
      const response = await axios.put(`http://127.0.0.1:5000/update_usr/${name}`, data, {withCredentials: true});
      console.log(response.data);
      alert('Credentials changed successfully');
      e.target.reset();
      } catch (error) {
       console.log(error);
      }
    };
  return (
    <Container>
    <Form method='post' onSubmit={handleOnsubmit}>
      <input type='text' placeholder='username' name='name' />
      <input type='text' placeholder='email' name='email' />
      <input type='text' placeholder='password' name='password' />
      <Send type='submit'>Send</Send>
    </Form>
    <Image>
      <img src={process.env.PUBLIC_URL + '/images/bg_settings.png'} alt='logo' />
    </Image>
</Container>
  )
}

export default Settings

const Container = styled.div`
display: flex;
align-items: center;
justify-content: space-between;
padding-left:38px;
`

const Form = styled.form`
width: 400px;
height: 75%;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;

input {
  margin-bottom: 30px;
  height: 38px;
  width: 360px;
  border: none;
  border-bottom: 2px solid #08711E;
  background: #dee2e6;
}

input:focus {
  outline: none;
}
`

const Image = styled.div`
width: 600px;
height: 80%;
display: flex;
align-items: center;
justify-content: center;
border-radius: 6px; 
`
const Send = styled.button`
  height: 38px;
  width: 360px;
  background: #08711E;
  margin-top: 30px;
  color: #fcfeff;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 3px;
  cursor: pointer;
  `