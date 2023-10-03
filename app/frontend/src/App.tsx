import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from "./pages/Home";
import Newsletter from "./pages/Newsletter";
import Main from "./pages/Main";
import Footer from "./components/Footer";
import Header from "./components/Header";
import "bootstrap/dist/css/bootstrap.min.css"
import React from 'react';

const App = () => {
  return (
    <div className="App">
      <Router>
      <Header />
        <Routes>
          <Route path="/" element={<Main />}/>
          <Route path="/newsletter" element={<Newsletter />}/>
        </Routes>
        <Footer />
      </Router>
    </div>
  );
}


export default App;
