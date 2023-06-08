import React from 'react'
import styled from 'styled-components';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PaymentsIcon from '@mui/icons-material/Payments';
import SettingsSuggestIcon from '@mui/icons-material/SettingsSuggest';

function Header() {
  return (
    <Container>
        <Welcome>Hello, Marrie</Welcome>
        <Icons>|<AccountCircleIcon />|<PaymentsIcon />|<SettingsSuggestIcon />|</Icons>
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