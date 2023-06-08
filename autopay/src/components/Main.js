import React from 'react'
import styled from 'styled-components'
import { dashboardNeed } from '../data/DashNeeds'
import HomeIcon from '@mui/icons-material/Home';
import DirectionsCarIcon from '@mui/icons-material/DirectionsCar';


function Main() {
  return (
    <Container>
      <Banner>
        <Automated>Automated Payments</Automated>
        <NeedsAuto>
          {
            dashboardNeed.map(item => (
              <Spesific>
                {item.icon}
                {item.text}
              </Spesific>
            ))
          }
        </NeedsAuto>
      </Banner>
      <PaymentsSide>
      <Table>
        <TitlePay>Cleared Payments</TitlePay>
        <Title>
          <One>Bill</One>
          <Two>Status</Two>
          <Three>Date</Three>
        </Title>
        <TableContent>
          <Icon><HomeIcon /></Icon>
          <Text>paid</Text>
          <Date>24/07/2023</Date>
        </TableContent>
      </Table>
      <Due>
        <DueTitle>Due Payments</DueTitle>
        <ThePay>
          <ItemVal>
            <DirectionsCarIcon />
          </ItemVal>
          <DueText> Transport</DueText>
        </ThePay>
      </Due>
      </PaymentsSide>
    </Container>
  )
}

export default Main

const Container = styled.div`

`
const Banner = styled.div`
color: #ffffff;
height: 25vh;
margin-top:15px;
margin-bottom:30px;
border-radius: 8px;
background: #08711E;
`
const Automated = styled.div`
font-weight: bold;
padding: 18px;
`
const NeedsAuto = styled.div`
display:flex;
align-items: center;
justify-content: space-around;

`
const Spesific = styled.div`
display: flex;
flex-direction: column;
align-items: center;
margin-top: 15px;
`
const PaymentsSide = styled.div`
height: 45vh;
display: grid;
grid-template-columns: 75% auto;
`

 const TitlePay = styled.div`
 font-weight: bold;
 margin: 15px;
 `

 const Table = styled.div`
 `

 const Title = styled.div`
 font-weight: bold;
 height: 38px;
 margin: 15px;
 display: flex;
 column-gap: 138px;
 justify-content: center;
 align-items: center;
 `
 const TableContent = styled.div`
 background: #ffffff;
 border-radius: 8px;
 height: 38px;
 margin: 15px;
 display: flex;
 column-gap: 138px;
 justify-content: center; 
 align-items: center;
 `

 const One = styled.div``

 const Two = styled.div``

 const Three = styled.div``

const Due = styled.div`
background: #ffffff;
border-radius: 8px;
padding-left: 28px;
`
const Icon = styled.div`
color: #08711E;
`

const Text = styled.div``

const Date = styled.div`

`

const DueTitle = styled.div`
font-weight: bold;
margin-bottom: 15px;
margin-top: 15px;
`

const ThePay = styled.div`
height: 74px;
display: flex;
align-items: center;
column-gap: 30px;
margin-right: 28px;
`

const ItemVal = styled.div`
background: #e5e5e5;
color: #08711E;
width: 54px;
height: 54px;
border-radius: 50%;
display: flex;
align-items: center;
justify-content: center;
`

const DueText = styled.div`

`