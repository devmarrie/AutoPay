import React, { useState } from 'react'
import styled from 'styled-components'
import { needsPresent } from '../data/NeedsData'

function Needs() {
  const [query, setQuery] = useState("");

  const search = (data) => {
    return data.filter((value) => value.need.toLowerCase().includes(query));
  };
  return (
    <ContainerNeeds>
     <NeedForm>
      <Fill>
        <Need>
          Need
          <input type='text' className='need' />
        </Need>
        <Amount>
          Amount
          <input type='text' className='amount' />
        </Amount>
        <DueDate>
          DueDate
          <input type='text' className='duedate' />
        </DueDate>
        <Reminder>
          Allow Reminder
          <input type='text' className='reminder' />
        </Reminder>
        <Buttons>
          <Add>Add</Add>
          <Cancel>Cancel</Cancel>
        </Buttons>
      </Fill>
     </NeedForm>
     <NeedTable>
      <SearchNeed>
        <input type='text' placeholder='search...'  className='search' 
                  onchange= {(e) => setQuery(e.target.value)}
                  /> 
      </SearchNeed>
      <ContentToNeedTable>
        <table data= {search(needsPresent)}>
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
                <td>{item.remove}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </ContentToNeedTable>
      </NeedTable>
    </ContainerNeeds>
  )
}

export default Needs

const ContainerNeeds = styled.div`

`
const NeedForm = styled.div`
display:flex;
justify-content: center;
margin-top: 20px;
height: 300px;
`

const Fill = styled.div`
background: #08711E;
border-radius: 6px;
color: #ffffff;
width:55%;
height: 300px;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
`

const NeedTable = styled.div`
`
const Need = styled.div`
display: flex;
flex-direction: column;
input {
  height:20px;
  width: 400px;
  margin-top: 10px;
  margin-bottom: 10px;
  border: none;

}

input:focus {
  outline: none;
}
`

const Amount = styled.div`
display: flex;
flex-direction: column;
input {
  height:20px;
  width: 400px;
  margin-top: 10px;
  margin-bottom: 10px;
  border: none;
}

input:focus {
  outline: none;
}
`

const DueDate = styled.div`
display: flex;
flex-direction: column;
input {
  height:20px;
  width: 400px;
  margin-top: 10px;
  margin-bottom: 10px;
  border: none;
}

input:focus {
  outline: none;
}
`

const Reminder = styled.div`
display: flex;
flex-direction: column;
input {
  height:20px;
  width: 400px;
  margin-top: 10px;
  margin-bottom: 10px;
  border: none;
}

input:focus {
  outline: none;
}
`
const Add = styled.div`
width: 92px;
height: 35px;
border-radius: 6px;
background: #000000;
color: #ffffff;
margin-right: 40px;
cursor: pointer;
display: flex;
align-items: center;
justify-content: center;
`

const Cancel = styled.div`
width: 92px;
height: 35px;
border-radius: 6px;
background: #000000;
color: #ffffff;
cursor: pointer;
display: flex;
align-items: center;
justify-content: center;
`

const Buttons  = styled.div`
display: flex;
`

const SearchNeed = styled.div`
display: flex;
height: 42px;
align-items: center;
justify-content: flex-end;
margin-top: 15px;

input {
  height:32px;
  border: none;
  border-radius: 25px;
  margin-right: 48px
}

input:focus {
  outline: none;
}
`

const ContentToNeedTable = styled.div`
margin-left: 15px;
margin-right: 15px;
margin-top: 15px;
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
 