import React, { useState } from 'react'
import styled from 'styled-components'
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { needsPresent } from '../data/NeedsData'

function Needs() {
  const [query, setQuery] = useState("");

  const search = (data) => {
    return data.filter((value) => value.need.toLowerCase().includes(query));
  };
  return (
    <ContainerNeeds>
      <NeedForm>
        <Form>
          <input type='text' placeholder='need name' className='need' />
          <input type='text' placeholder='amount' className='amount' />
          <input type='text' placeholder='due date(24-06-2023)' className='duedate' />
          <Send>Send</Send>
        </Form>
        <Picture>
          <Imgc>
             <img src={process.env.PUBLIC_URL + '/images/new_found_person.png'} alt='logo' />
          </Imgc>
        </Picture>
      </NeedForm>
      <NeedTable>
      <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell style={{fontWeight: 'bold'}}>Need</TableCell>
            <TableCell align="right" style={{fontWeight: 'bold'}}>Amount</TableCell>
            <TableCell align="right" style={{fontWeight: 'bold'}}>Due Date</TableCell>
            <TableCell align="right" style={{fontWeight: 'bold'}}>Remove</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
         {needsPresent.map((item) => (
          <TableRow
           key={item.need}
           sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
          >
          <TableCell component="th" scope="row">
                {item.need}
          </TableCell>
          <TableCell align="right">{item.amount}</TableCell>
          <TableCell align="right">{item.duedate}</TableCell>
          <TableCell align="right">{item.remove}</TableCell>
          </TableRow>
         ))}
         </TableBody>
         </Table>
         </TableContainer>
      {/* <ContentToNeedTable>
        <table>
        <tbody>
            <tr>
              <th>Need</th>
              <th>Amount</th>
              <th>Due Date</th>
              <th>Reminder Date</th>
              <th> Action</th>
            </tr>
            {needsPresent.map((item) => (
              <tr>
                <td>{item.need}</td>
                <td>{item.amount}</td>
                <td>{item.duedate}</td>
                <td>{item.reminderdate}</td>
                <td><Toa>{item.remove}</Toa></td>
              </tr>
            ))}
          </tbody>
        </table>
      </ContentToNeedTable> */}
      </NeedTable>
    </ContainerNeeds>
  )
}

export default Needs

const ContainerNeeds = styled.div`
display: grid;
grid-template-rows: 300px auto;
`
const NeedForm = styled.div`
display: flex;
`
const Form = styled.div`
width: 50%;
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
const Picture = styled.div`
display: flex;
justify-content: center;
align-items: center;
`
const Imgc = styled.div`
width:400px;
height: 400px;
img {
  width: 100%;
}
`

const Send = styled.div`
  height: 38px;
  width: 360px;
  background: #08711E;
  color: #fcfeff;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 3px;
  cursor: pointer;
  `


const NeedTable = styled.div`
display: flex;
justify-content: center;
align-items: center;
padding-left: 28px;
padding-right: 28px;
`

const ContentToNeedTable = styled.div`
width:65%
height:300px;
table {
  width: 100%;
  border-spacing: 15px;
  border-radius: 6px;
  color: #444;
  background: #ffffff;
}

tr {
  margin-bottom: 20px;
}

th {
  width: 250px;
  text-align: left;
  font-size: 20px;
}

td {
  width: 200px;
  font-size: 20px;
}
`
const Toa = styled.div`
background: #ea1535;
width:68px;
height:42px;
cursor: pointer;
display: flex;
align-items: center;
justify-content: center;
padding-left: 5px;
padding-right: 5px;
border-radius: 6px;
`
