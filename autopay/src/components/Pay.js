import React from 'react'
import styled from 'styled-components'
import axios from 'axios';

function Pay() {
  const handleOnsubmit = async (e) => {
    e.preventDefault();
    // const sessionToken = localStorage.getItem('user_id');
    console.log(e.target)
    const need = e.target.need.value;
    const amount = e.target.amount.value;
    const number = e.target.number.value;
    const code = e.target.code.value;

    const data = {
      "need": need,
      "amount": amount,
      "number": number,
      "code": code
    };

    try {
      const response = await axios.post('http://127.0.0.1:5000/create_pay', data, {withCredentials: true});
      console.log(response.data);
      alert('Payment details registered successfully');
      e.target.reset();
      } catch (error) {
       console.log(error);
      }
    };
  return (
    <Container>
        <Form method='post' onSubmit={handleOnsubmit}>
          <input type='text' placeholder='needName' name='need' />
          <input type='text' placeholder='amount' name='amount' />
          <input type='text' placeholder='mpesaNumber' name='number' />
          <input type='text' placeholder='mpesaCode' name='code' />
          <Send type='submit'>Send</Send>
        </Form>
        <Image>
          <img src={process.env.PUBLIC_URL + '/images/monies.png'} alt='logo' />
        </Image>
    </Container>
  )
}

export default Pay

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

const PayCont = styled.div`
width: 400px;
height: 400px;
color: #ffffff;
background: #08711E;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap: 30px;
`
const Type = styled.div``

const Details = styled.div``

const Transact = styled.div`
display: flex;
flex-direction: column;
input {
    border: none;
    margin-top: 15px;
}

input:focus {
    outline: none;
}
`