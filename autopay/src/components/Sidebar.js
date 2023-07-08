import React, {useState} from 'react'
import styled from 'styled-components'
import {sidebarItems} from '../data/SidebarData'
import LogoutIcon from '@mui/icons-material/Logout';
import { useNavigate } from 'react-router-dom';


function Sidebar() {
  const navigate = useNavigate()
  const [selectedItem, setSelectedItem] = useState(null);

  const handOnClickIt = (route, index) => {
    setSelectedItem(index)
    navigate(route);
  }

  const handleLogout = () => {
    navigate('/')
  }
  return (
    <Container>
        <Logo>
            <Img>
               <img src={process.env.PUBLIC_URL + '/images/autopaylogo.png'} alt='logo' />
            </Img>
            <Text>AutoPay</Text>
        </Logo>
        <Pages>
            {
              sidebarItems.map((item, index) => (
                <Channel 
                key={index} 
                onClick={() => handOnClickIt(item.route, index)}
                style={{
                  backgroundColor: selectedItem === index ? '#08711E' : 'transparent',
                  color: selectedItem === index ? '#ffffff' : 'black'
                }}
                >
                  {item.icon}
                  {item.text}
                </Channel>
              ))
            }
        </Pages>
        <Stroke>
          <Line></Line>
        </Stroke>
        <Signout>
          <Channel onClick={ handleLogout }>
            <LogoutIcon />
            Log Out
          </Channel>
        </Signout>
    </Container>
  )
}

export default Sidebar

const Container = styled.div`
background: #fcfeff;
`
const Logo = styled.div`
height: 95px;
display: flex;
align-items: center;
margin-bottom: 22px;
margin-left: 28px;
padding-top: 10px;
`
const Img = styled.div`
width: 68px;
height: 68px;
img {
    width:100%;
}
`
const Text = styled.div`
margin-left:0px;
`
const Pages = styled.div`
margin-bottom: 104px;
`

const Channel = styled.div`
height: 28px;
width: 75%;
display: grid;
grid-template-columns: 15% auto;
align-items: center;
padding:8px;
border-radius: 3px;
cursor: pointer;
margin-left: 28px;

:hover {
  background: #08711E;
  color: #ffffff;
}

`

const Stroke = styled.div`
margin-left: 28px;
margin-right: 28px;

`

const Line = styled.div`
width:100%;
height: 1px;
background-color: black;
`

const Signout = styled.div`
margin-top: 68px;
`
