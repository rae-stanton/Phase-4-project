import React from "react";
import { Formik, Field, Form } from "formik";
import Button from "react-bootstrap/Button";
import loginImage from "../images/login.png"; // Importing the image
import "./Login.css";

function Login() {
  return (
    <div className="login-form">
      <div className="login-content">
        <h1>Log in here:</h1>
        <Formik
          initialValues={{
            firstName: "",
            lastName: "",
            email: "",
          }}
          onSubmit={async (values) => {
            await new Promise((r) => setTimeout(r, 500));
            alert(JSON.stringify(values, null, 2));
          }}
        >
          <Form className="form-border">
            <img
              src={loginImage}
              alt="Login Illustration"
              className="login-image"
            />
            <br />

            <label htmlFor="firstName">First Name</label>
            <br />
            <Field id="firstName" name="firstName" placeholder="Luna" />
            <br />
            <label htmlFor="lastName">Last Name</label>
            <br />
            <Field id="lastName" name="lastName" placeholder="Lucy" />
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
