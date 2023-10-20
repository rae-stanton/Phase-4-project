import React from "react";
import { Formik, Field, Form } from "formik";
import Button from "react-bootstrap/Button";
import loginImage from "../images/login.png";
import "./Login.css";

function Login() {
  const handleLogin = async (values) => {
    try {
      // Make a POST request to the Flask API endpoint
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      });

      if (response.ok) {
        const data = await response.json();

        if (data && data.access_token) {
          // Save the token to local storage or to state
          localStorage.setItem('access_token', data.access_token);
          alert("Logged in successfully!");
        } else {
          alert("Failed to log in.");
        }
      } else {
        alert("Error logging in. Check your email and password.");
      }
    } catch (error) {
      console.error("There was an error logging in:", error);
      alert("There was an error logging in.");
    }
  };

  return (
    <div className="login-form">
      <div className="login-content">
        <h1>Log in here:</h1>
        <Formik
          initialValues={{
            email: "",
            password: "",
          }}
          onSubmit={handleLogin}
        >
          <Form className="form-border">
            <img
              src={loginImage}
              alt="Login Illustration"
              className="login-image"
            />
            <br />
            <label htmlFor="email">Email</label>
            <br />
            <Field
              id="email"
              name="email"
              placeholder="LuneCy@acme.com"
              type="email"
            />
            <br />
            <label htmlFor="password">Password</label>
            <br />
            <Field
              id="password"
              name="password"
              placeholder="Enter your password"
              type="password"
            />
            <br />
            <br />
            <Button variant="primary" type="submit" className="form-button">
              Log In
            </Button>
            <br />
          </Form>
        </Formik>
      </div>
    </div>
  );
}

export default Login;
