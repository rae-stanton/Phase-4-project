// import React from "react";
// import { Formik, Field, Form } from "formik";
// import Button from "react-bootstrap/Button";
// import loginImage from "../images/login.png"; // Importing the image
// import "./Login.css";

// function Register() {
//   return (
//     <div className="register-form">
//       <div className="register-content">
//         <h1>Register here:</h1>
//         <Formik
//           initialValues={{
//             firstName: "",
//             lastName: "",
//             email: "",
//             password: "",
//           }}
//           onSubmit={async (values) => {
//             const response = await fetch('http://127.0.0.1:5000/register', {
//               method: 'POST',
//               mode: "cors",
//               headers: {
//                 'Content-Type': 'application/json',
//               },
//               body: JSON.stringify({
//                 name: `${values.firstName} ${values.lastName}`,
//                 email: values.email
//               }),
//             });

//             const data = await response.json();

//             if (response.status === 200) {
//               // Handle successful registration (e.g., redirect to login or dashboard)
//               alert("Registration successful!");
//             } else {
//               // Handle any errors from the server
//               alert(data.message || "Registration failed.");
//             }
//           }}
//         >
//           <Form className="form-border">
//             <img
//               src={loginImage}
//               alt="Login Illustration"
//               className="login-image"
//             />
//             <br />

//             <label htmlFor="firstName">First Name</label>
//             <br />
//             <Field id="firstName" name="firstName" placeholder="Luna" />
//             <br />
//             <label htmlFor="lastName">Last Name</label>
//             <br />
//             <Field id="lastName" name="lastName" placeholder="Lucy" />
//             <br />
//             <label htmlFor="email">Email</label>
//             <br />
//             <Field
//               id="email"
//               name="email"
//               placeholder="Luna@acme.com"
//               type="email"
//             />
//             <br />
//             <label htmlFor="password">Password</label>
//             <br />
//             <Field
//               id="password"
//               name="password"
//               placeholder="********"
//               type="password"
//             />
//             <br />
//             <br />
//             <Button variant="primary" type="submit" className="form-button">
//               Register
//             </Button>
//             <br />
//           </Form>
//         </Formik>
//       </div>
//     </div>
//   );
// }

// export default Register;
