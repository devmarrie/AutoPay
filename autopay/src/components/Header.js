import React from 'react'
import styled from 'styled-components';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PaymentsIcon from '@mui/icons-material/Payments';
import SettingsSuggestIcon from '@mui/icons-material/SettingsSuggest';
import { useNavigate } from 'react-router-dom';

function Header() {
  const navigate = useNavigate();
  const handleAccountClick = () => {
    navigate('/dashboard');
  };

  const handlePaymentsClick = () => {
    navigate('/pay');
  };

  const handleSettingsClick = () => {
    navigate('/settings');
  };
  return (
    <Container>
        <Welcome>Hello, Automator</Welcome>
        <Icons>
          |
          <ClickableIcon onClick={handleAccountClick}><AccountCircleIcon /></ClickableIcon> 
          |
          <ClickableIcon onClick={handlePaymentsClick}><PaymentsIcon /></ClickableIcon>
          |
          <ClickableIcon onClick={handleSettingsClick}><SettingsSuggestIcon /></ClickableIcon> 
          |
        </Icons>
    </Container>
  )
}

export default Header

const Container = styled.div`
display: flex;
flex-direction: row;
align-items: flex-end;
justify-content: space-between;
`
const Welcome = styled.div``
const Icons = styled.div`
display:flex;
align-items:center;
gap: 10px;
`
const ClickableIcon = styled.span`
  cursor: pointer;
`