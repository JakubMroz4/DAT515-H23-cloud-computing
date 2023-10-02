import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from "./pages/Home";
import Newsletter from "./pages/Newsletter";
import Footer from "./components/Footer";
import Header from "./components/Header";
import Signup from "./pages/Signup";
import Login from "./pages/Login";
import "bootstrap/dist/css/bootstrap.min.css"

function App() {
  return (
    <div className="App">
      <Router>
        <Header />
        <Routes>
          <Route path="/" element={<Home />}/>
          <Route path="/newsletter" element={<Newsletter />}/>
          <Route path="/register" element={<Signup />}/>
          <Route path="/login" element={<Login />}/>
        </Routes>
        <Footer />
      </Router>
    </div>
  );
}


export default App;
