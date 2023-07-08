import React from 'react'
import styled from 'styled-components'

function NotFound() {
  return (
    <Container> 404 Not Found</Container>
  )
}

export default NotFound

const Container = styled.div`
font-weight: bold;
font-size: 24px;
display: flex;
padding-top: 10px;
justify-content: center;
`