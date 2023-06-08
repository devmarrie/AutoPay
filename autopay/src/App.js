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

function App() {
  return (
    <div className="App">
      <Router>
        <Container>
          <Sidebar />
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/history" element={<Payments />} />
            <Route path="/needs" element={<Needs />} />
            <Route path="/pay" element={<Pay />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </Container>
      </Router>
    </div>
  );
}

export default App;

const Container = styled.div`
width: 100%;
height: 100vh;
display: grid;
background: #dee2e6;
grid-template-columns: 260px auto;
`
