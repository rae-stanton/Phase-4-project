import React, { useState } from "react";
import { Formik, Field, Form } from "formik";
import Button from "react-bootstrap/Button";
import loginImage from "../images/login.png";
import "./Login.css";

function Login() {
  const [message, setMessage] = useState("");

  const handleLoginSubmit = async (values) => {
    // Reset any existing message
    setMessage("");

    try {
      const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();

      if (data.access_token) {
        localStorage.setItem("token", data.access_token);
        setMessage("Successfully logged in!");
      } else {
        setMessage("Failed to log in. Please try again.");
      }
    } catch (error) {
      console.error("There was an error logging in:", error);
      setMessage(
        "Failed to log in. Please check your connection and try again."
      );
    }
  };

  return (
    <div className="login-form">
      <div className="login-content">
        <h1>Log in here:</h1>
        {message && <div className="message">{message}</div>}
        <Formik
          initialValues={{
            email: "",
            password: "",
          }}
          onSubmit={handleLoginSubmit}
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
