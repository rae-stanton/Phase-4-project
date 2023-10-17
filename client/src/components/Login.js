import React from 'react';
import { Formik, Field, Form } from 'formik';

function Login() {
  return (
    <div>
      <h1>Log in here:</h1>
      <Formik
        initialValues={{
          firstName: '',
          lastName: '',
          email: '',
        }}
        onSubmit={async (values) => {
          await new Promise((r) => setTimeout(r, 500));
          alert(JSON.stringify(values, null, 2));
        }}
      >
        <Form>
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
          <button type="submit">Submit</button>
          <br />
        </Form>
      </Formik>
    </div>
  );
}

export default Login;
