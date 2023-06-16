import React from 'react'
import styled from 'styled-components'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'



function Login() {
  const navigate = useNavigate();
  const handleOnsubmit = async (e) =>{
    e.preventDefault();
    const username = e.target.username.value;
    const password = e.target.password.value;
  
    const data = {
      "username": username,
      "password": password,
    };
    try {
      const response = await axios.post('http://127.0.0.1:5000/login', data);
      console.log(response.data)
      alert("Succesfully Logged in. Please create needs to proceed!");
      e.target.reset();
      navigate('/needs');
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <Kishikio>
      <Container>
        <Picture><img src={process.env.PUBLIC_URL + '/images/mwosho.png'} alt='logo' /></Picture>
        <Details>
          <Text> Log In</Text>
          <OtherSide method='post' onSubmit={handleOnsubmit}>
          <input type='text' placeholder='user name' name='username' />
          <input type='text' placeholder='password' name='password' />
          <Send type='submit'>
            Login
          </Send>
          </OtherSide>
        </Details>
      </Container>
    </Kishikio>
    
  )
}

export default Login

const Kishikio = styled.div`
display: flex;
align-items: center;
justify-content: center;
`
const Container = styled.div`
width: 80%;
height: 80%;
display: flex;
align-items: center;
justify-content: space-evenly;
`

const Picture = styled.div`
width: 450px;
height: 450px;
img {
  width: 100%;
}
`

const Details = styled.div`
width: 400px;
height: 400px;
background: #fcfeff;
border-radius: 6px;
border: 1px solid grey;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;

`
const OtherSide = styled.form`
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
input {
  height: 38px;
  width: 300px;
  margin-bottom: 28px;
}
input:focus {
  outline: none;
} 
`
const Text = styled.div`
font-wieght: 600;
font-size: 1.8rem;
font-family: Sans-serif;
margin-bottom: 28px;
`
const Send = styled.button`
  height: 38px;
  width: 315px;
  background: #08711E;
  color: #fcfeff;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 25px;
  cursor: pointer;
  `