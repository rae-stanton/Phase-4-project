import React from "react";
import { Link } from "react-router-dom";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import "./AppNavbar.css"

function AppNavbar() {
  return (
    <Navbar className="main-navbar" expand="lg">
      <Container className="d-flex justify-content-between">
        {/* Other Navbar content, like a potential brand, would go here.
         Also need to fix styling to see fit.
        */}
        <Nav className="flex-grow-1 justify-content-end align-items-center">
          <Nav.Link as={Link} to="/" style={{ marginRight: '10px' }} className="navlink">Home</Nav.Link>
          <Nav.Link as={Link} to="/Dashboard" style={{ marginRight: '10px' }} className="navlink">Dashboard</Nav.Link>
          <Nav.Link as={Link} to="/Login" className="navlink">Login</Nav.Link>
          <Nav.Link as={Link} to="/Register" className="navlink">Register</Nav.Link>
          <Nav.Link as={Link} to="/Cart" className="navlink">Cart (0)</Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
}

export default AppNavbar;



