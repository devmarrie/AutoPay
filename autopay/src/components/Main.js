import React, {useState, useEffect} from 'react'
import styled from 'styled-components'
import PaymentsIcon from '@mui/icons-material/Payments';
import DirectionsCarIcon from '@mui/icons-material/DirectionsCar';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import HomeIcon from '@mui/icons-material/Home';
import WaterDropOutlinedIcon from '@mui/icons-material/WaterDropOutlined';
import EmojiObjectsOutlinedIcon from '@mui/icons-material/EmojiObjectsOutlined';
import WifiOutlinedIcon from '@mui/icons-material/WifiOutlined';
import SchoolIcon from '@mui/icons-material/School';
import SubscriptionsIcon from '@mui/icons-material/Subscriptions';
import SportsGymnasticsIcon from '@mui/icons-material/SportsGymnastics';
import AddToPhotosIcon from '@mui/icons-material/AddToPhotos';
import FoodBankIcon from '@mui/icons-material/FoodBank';


const iconMap = {
  rent: <HomeIcon />,
  water: <WaterDropOutlinedIcon />,
  lights: <EmojiObjectsOutlinedIcon />,
  wifi: <WifiOutlinedIcon />,
  fees: <SchoolIcon />,
  subscriptions: <SubscriptionsIcon />,
  transport: <DirectionsCarIcon />,
  gym: <SportsGymnasticsIcon />,
  food: <FoodBankIcon />,
  any: <AddToPhotosIcon />
};

function Main() {
  const [payments, setPayments] =  useState([])
  const navigate = useNavigate();
  const seeAll = () => {
    navigate("/history")
  }
  const fetchPayments = async () => {
    const response = await axios.get('http://127.0.0.1:5000/get_payments');
    const resdata = response.data
    setPayments(resdata)
    console.log(resdata)
  };

  useEffect(() => {
    fetchPayments();
  },[])
  const limitPaymnets = payments.slice(0,3);
  console.log(limitPaymnets)
  //Needs
  const [needs, setNeeds] =  useState([])
  const fetchData = async () => {
    const response = await axios.get('http://127.0.0.1:5000/get_needs');
    const resdata = response.data
    setNeeds(resdata)
    console.log("res:", response.data)
  };


  useEffect(() => {
    fetchData();
  }, []);
  const limitNeedsBanner = needs.slice(0,6);
  const limitNeedsDue = needs.slice(0,3);
  return (
    <Container>
      <Banner>
        <Automated>Automated Payments</Automated>
        <NeedsAuto>
          {
            limitNeedsBanner.map((item, index) => (
              <Spesific key={index}>
                {iconMap[item.need] || iconMap.any}
                {item.need}
              </Spesific>
            ))
          }
        </NeedsAuto>
      </Banner>
      <PaymentsSide>
      <Table>
        <TitlePay>Cleared Payments</TitlePay>
        <Title>
          <One>Icon</One>
          <Two>Need</Two>
          <Three>Amount</Three>
          <Three>Code</Three>
        </Title>
          {
            limitPaymnets.map((pay) => (
              <TableContent>
              <Icon><PaymentsIcon /></Icon>
              <Text>{pay.need}</Text>
              <Date>{pay.amount}</Date>
              <Text>{pay.code}</Text>
              </TableContent>
            ))
          }
          <More onClick={seeAll}>See All</More>
      </Table>
      <Due>
        <DueTitle>Due Payments</DueTitle>
        {
          limitNeedsDue.map((due) => (
            <ThePay>
             <ItemVal>
             {iconMap[due.need] || iconMap.any}
             </ItemVal>
             <DueText>{due.need}</DueText>
           </ThePay>
          ))
        }
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
 justify-content: space-between; 
 align-items: center;
 padding-left: 38px;
 padding-right: 10px;

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
const More = styled.div`
cursor: pointer;
height: 38px;
display: flex;
align-items: center;
justify-content: center;
font-weight: 500;
`