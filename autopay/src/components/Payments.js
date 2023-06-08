import React from 'react'
import styled from 'styled-components';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import YoutubeSearchedForIcon from '@mui/icons-material/YoutubeSearchedFor';

function createData(name, total, method) {
  return {
    name,
    total,
    method,
    history: [
       {
        date: '2022-01-06',
        to: 'Greenhouse Apartments',
        amount: 20500
       },
       {
        date: '2022-01-05',
        to: 'Greenhouse Apartments',
        amount: 20500
       },
       {
        date: '2022-01-04',
        to: 'Greenhouse Apartments',
        amount: 20500
       },
    ],
  };
}

function Row(props) {
  const { row } = props;
  const [open, setOpen] = React.useState(false);

  return (
    <React.Fragment>
      <TableRow sx={{ '& > *': { borderBottom: 'unset' } }}>
        <TableCell>
          <IconButton
            aria-label="expand row"
            size="small"
            onClick={() => setOpen(!open)}
          >
            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
        </TableCell>
        <TableCell component="th" scope="row">
          {row.name}
        </TableCell>
        <TableCell align="right">{row.total}</TableCell>
        <TableCell align="right">{row.method}</TableCell>
      </TableRow>
      <TableRow>
        <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <Box sx={{ margin: 1 }}>
              <Typography variant="h6" gutterBottom component="div">
                History
              </Typography>
              <Table size="small" aria-label="purchases">
                <TableHead>
                  <TableRow >
                    <TableCell style={{ fontWeight: 'bold' }}>Date</TableCell>
                    <TableCell style={{ fontWeight: 'bold' }}>Recipient</TableCell>
                    <TableCell style={{ fontWeight: 'bold' }} align="right">Amount</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {row.history.map((historyRow) => (
                    <TableRow key={historyRow.date}>
                      <TableCell component="th" scope="row">
                        {historyRow.date}
                      </TableCell>
                      <TableCell>{historyRow.to}</TableCell>
                      <TableCell align="right">{historyRow.amount}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Box>
          </Collapse>
        </TableCell>
      </TableRow>
    </React.Fragment>
  );
}

Row.propTypes = {
  row: PropTypes.shape({
    total: PropTypes.number.isRequired,
    method: PropTypes.string.isRequired,
    history: PropTypes.arrayOf(
      PropTypes.shape({
        amount: PropTypes.number.isRequired,
        to: PropTypes.string.isRequired,
        date: PropTypes.string.isRequired,
      }),
    ).isRequired,
    name: PropTypes.string.isRequired,
  }).isRequired,
};

const rows = [
  createData('Wifi', 12500, 'M-Pesa'),
  createData('Rent', 150000, 'M-pesa'),
  createData('Transport', 14000, 'M-pesa'),
  createData('Food', 13500,'Bank'),
  createData('Gym', 1200, 'M-pesa'),
];


function Payments( ) {
  return (
    <Container>
      <JustViews>
        <SearchConatiner>
          <input type="text" placeholder='Search..' className='Search' />
          <YoutubeSearchedForIcon />
        </SearchConatiner>        
      </JustViews>
      <Kasuku>
      <TableContainer component={Paper}>
    <Table aria-label="collapsible table">
      <TableHead>
        <TableRow>
          <TableCell />
          <TableCell style={{ fontWeight: 'bold' }}>Need</TableCell>
          <TableCell style={{ fontWeight: 'bold' }} align="right">Total</TableCell>
          <TableCell style={{ fontWeight: 'bold' }} align="right">Method</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {rows.map((row) => (
          <Row key={row.name} row={row} />
        ))}
      </TableBody>
    </Table>
  </TableContainer>
    </Kasuku>
    </Container>
  );
}

export default Payments

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

