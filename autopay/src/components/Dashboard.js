import React from 'react'
import styled from 'styled-components';
import Header from './Header';
import Main from './Main';

function Dashboard() {
  return (
    <div>
      <ContainDash>
        <Header />
        <Main />
      </ContainDash>
    </div>
  )
}

export default Dashboard

const ContainDash = styled.div`
display: grid;
grid-template-rows 75px auto;
margin-right: 32px;
margin-left: 32px;
`