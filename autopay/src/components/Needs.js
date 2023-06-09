import styled from 'styled-components'
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import axios from 'axios';
import { useState, useEffect } from "react"


function Needs() {
  const [needs, setNeeds] =  useState([])
  const fetchData = async () => {
    const response = await axios.get('http://127.0.0.1:5000/get_needs');
    const resdata = response.data
    setNeeds(resdata)
    console.log("res:", response.data)
  };


  const handleOnsubmit = async (e) => {
    e.preventDefault();
    // const sessionToken = localStorage.getItem('user_id');
    console.log(e.target)
    const need = e.target.need.value;
    const amount = e.target.amount.value;
    const phone_no = e.target.phone_no.value;
    const duedate = e.target.duedate.value;

    const data = {
      "need": need,
      "amount": amount,
      "phone_no": phone_no,
      "duedate": duedate
    };

    try {
      const response = await axios.post('http://127.0.0.1:5000/add_need', data, {withCredentials: true});
      console.log(response.data);
      alert('Need created successfully');
      fetchData();
      e.target.reset();
      // the table
      } catch (error) {
       console.log(error);
      }
    };

    useEffect(() => {
      fetchData();
    }, []);

  return (
    <ContainerNeeds>
      <NeedForm>
        <Form method='post' onSubmit={handleOnsubmit}>
          <input type='text' placeholder='need' name='need' />
          <input type='text' placeholder='amount' name='amount' />
          <input type='text' placeholder='phoneNumber' name='phone_no' />
          <input type='text' placeholder='duedate(18:42:00 12-06-2023)' name='duedate' />
          <Send type='submit'>Send</Send>
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
            <TableCell align="right" style={{fontWeight: 'bold'}}>PhoneNumber</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
         {needs.map((val) => (
          <TableRow
           key={val.need}
           sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
          >
          <TableCell component="th" scope="row">
                {val.need}
          </TableCell>
          <TableCell align="right">{val.amount}</TableCell>
          <TableCell align="right">{val.duedate}</TableCell>
          <TableCell align="right">{val.phone_no}</TableCell>
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
margin-top: 28px;
margin-bottom: 8px;
`
const Form = styled.form`
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

const Send = styled.button`
  height: 42px;
  width: 370px;
  background: #08711E;
  color: #fcfeff;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  cursor: pointer;
  `


const NeedTable = styled.div`
margin: 16px;

`


// const Toa = styled.div`
// background: #ea1535;
// width:68px;
// height:42px;
// cursor: pointer;
// display: flex;
// align-items: center;
// justify-content: center;
// padding-left: 5px;
// padding-right: 5px;
// border-radius: 6px;
// `
