import React, { useState, useEffect} from 'react'
import styled from 'styled-components';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import axios from 'axios';

function History( ) {
  const [query, setQuery] = useState("");
  const [payments, setPayments] =  useState([])
  const fetchPayments = async () => {
    const response = await axios.get('http://127.0.0.1:5000/get_payments');
    const resdata = response.data
    setPayments(resdata)
    console.log(resdata)
  };

  useEffect(() => {
    fetchPayments();
  },[])
  return (
    <Container>
      <JustViews>
        <SearchConatiner>
          <input 
          type="text" 
          placeholder='Enter the need to search...' 
          className='Search' 
          onChange={(e) => setQuery(e.target.value)}
          />
          <Search type='submit'>Search</Search>
        </SearchConatiner>        
      </JustViews>
      <Kasuku>
      <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell style={{fontWeight: 'bold'}}>Need</TableCell>
            <TableCell align="right" style={{fontWeight: 'bold'}}>Amount</TableCell>
            <TableCell align="right" style={{fontWeight: 'bold'}}>NumberUsedToPay</TableCell>
            <TableCell align="right" style={{fontWeight: 'bold'}}>MpesaCode</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
         {payments.filter(d => d.need.toLowerCase().includes(query)).map((val) => (
          <TableRow
           key={val.need}
           sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
          >
          <TableCell component="th" scope="row">
                {val.need}
          </TableCell>
          <TableCell align="right">{val.amount}</TableCell>
          <TableCell align="right">{val.number}</TableCell>
          <TableCell align="right">{val.code}</TableCell>
          </TableRow>
         ))}
         </TableBody>
         </Table>
         </TableContainer>
      </Kasuku>
    </Container>
  );
}

export default History

const Kasuku = styled.div`
`
const Container = styled.div`
padding-left: 28px;
padding-right: 28px;
display: grid;
grid-template-rows 15% auto;
`

const JustViews = styled.div`
margin-bottom: 15px;
margin-top: 15px;
display: flex;
align-items: center;
justify-content: space-between;
`

const SearchConatiner = styled.div`
height: 38px;
width: 600px;
border-radius: 25px;
background: #ffffff;
box-shadow: inset 0 0 0 1px #08711E;
font-weight: normal;
display: flex;
align-items: center;
justify-content: space-between;
padding-left: 8px;
padding-right: 16px;

input {
  background-color: transparent;
  border: none;
}

input:focus {
  outline: none;
}
`
const Search = styled.button`
width: 150px;
height: 30px;
background:#08711E;
border-radius: 25px;
color: white;
`
