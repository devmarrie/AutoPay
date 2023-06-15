import React from 'react'
import styled from 'styled-components'

function Pay() {
  return (
    <Container>
        <Form>
          <input type='text' placeholder='need name' className='need' />
          <input type='text' placeholder='amount' className='amount' />
          <input type='text' placeholder='mpesa number' className='mpesa_number' />
          <input type='text' placeholder='mpesa code' className='mpesa_code' />
          <Send>Send</Send>
        </Form>
        <Image>
          <img src={process.env.PUBLIC_URL + '/images/monies.png'} alt='logo' />
        </Image>
        {/* <PayCont>
            <Type>Rent</Type>
            <Details>
                Amount:
                5500
            </Details>
            <Transact>
                Mpesa.no
                <input type='text' placeholder='0712345678' className='number' />
            </Transact>
        </PayCont> */}
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

const Form = styled.div`
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
const Send = styled.div`
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