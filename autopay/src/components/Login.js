import React from 'react'
import styled from 'styled-components'
import axios from 'axios'
import { useNavigate } from 'react-router-dom';


function Login() {
  const navigate = useNavigate();
  const handleOnClick = () => {
    axios.get('http://127.0.0.1:5000/login', { withCredentials: true })
    .then(response => {
      console.log(response);
      navigate('/needs')
    })
    .catch(error => {
      console.error(error);
    });
  };
  // const handleOnsubmit = async (e) =>{
  //   e.preventDefault();
  //   const username = e.target.username.value;
  //   const phone_no = e.target.phone_no.value;
  //   const password = e.target.password.value;
  
  //   const data = {
  //     "username": username,
  //     "password": password,
  //     "phone_no": phone_no
  //   };
  //   try {
  //     console.log(data)
  //     const response = await axios.post('http://127.0.0.1:5000/register', data);
  //     console.log(response.data)
  //     alert("User registered successfully!");
  //     e.target.reset();
  //     navigate('/user');
  //   } catch (error) {
  //     console.log(error);
  //   }
  // }

  return (
    <Kishikio>
      <Container>
        <Picture><img src={process.env.PUBLIC_URL + '/images/user_dashboard.png'} alt='logo' /></Picture>
        <Details>
          <Text> Sign In for Autopay</Text>
          <OtherSide>
          {/* <input type='text' placeholder='user name' name='username' />
          <input type='text' placeholder='phone number(254712345678)' name='phone_no' />
          <input type='text' placeholder='password' name='password' /> */}
          <Send type='submit' onClick={handleOnClick}>
            Sign In with Google
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
margin-top:120px;
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
const OtherSide = styled.div`
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
