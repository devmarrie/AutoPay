import React from 'react'
import styled from 'styled-components'

function Pay() {
  return (
    <Container>
        <PayCont>
            <Type>Rent</Type>
            <Details>
                Amount:
                5500
            </Details>
            <Transact>
                Mpesa.no
                <input type='text' placeholder='0712345678' className='number' />
            </Transact>
        </PayCont>
    </Container>
  )
}

export default Pay

const Container = styled.div`
display: flex;
align-items: center;
justify-content: center;
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