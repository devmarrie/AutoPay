import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import Payments from './components/Payments';
import Needs from './components/Needs';
import Settings from './components/Settings';
import Sidebar from './components/Sidebar';
import styled from 'styled-components';
import Pay from './components/Pay';
import LogInUser from './components/LogInUser';


function App() {
  return (
    <div className="App">
      <Container>
        <Room>
          <Sidebar />
          <Router>
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/user" element={<LogInUser />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/history" element={<Payments />} />
            <Route path="/needs" element={<Needs />} />
            <Route path="/pay" element={<Pay />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
          </Router>
        </Room>
      </Container>  
    </div>
  );
}


export default App;

const Container = styled.div`
background: #dee2e6;
width: 100%;
height: 100vh;

`
const Room = styled.div`
width: 100%;
height: 100vh;
display: grid;
grid-template-columns: 260px auto;
`
