import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./Home";
import Dashboard from "./Dashboard";
import Login from "./Login";
import AppNavbar from "./AppNavbar";
import Register from "./Register"
import EditUser from "./EditUser";

function App() {
  return (
    <Router>
      <div>
        {/* Navigation */}
        <AppNavbar />

        {/* Routing Configuration */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/login" element={<Login />} />
          <Route path="/edituser/:userId" element={<EditUser />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
