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
      <Container>
        <Router>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route element={<RoomWithSidebar />}>
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/history" element={<Payments />} />
              <Route path="/needs" element={<Needs />} />
              <Route path="/pay" element={<Pay />} />
              <Route path="/settings" element={<Settings />} />
            </Route>
          </Routes>
        </Router>
      </Container>
    </div>
  );
}

export default App;

const Container = styled.div`
  background: #dee2e6;
  width: 100%;
  height: 100vh;
`;

const Home = () => {
  return <Login />;
};

const RoomWithSidebar = () => {
  return (
    <StyledRoom>
      <Sidebar />
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/history" element={<Payments />} />
        <Route path="/needs" element={<Needs />} />
        <Route path="/pay" element={<Pay />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </StyledRoom>
  );
};

const StyledRoom = styled.div`
  width: 100%;
  height: 100vh;
  display: grid;
  grid-template-columns: 260px auto;
`;