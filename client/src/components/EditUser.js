import React, { useState, useEffect } from "react";
import { Formik, Field, Form } from "formik";
import Button from "react-bootstrap/Button";
import { useParams } from 'react-router-dom';

function EditUser(props) {
  const { userId } = useParams();
  const [userData, setUserData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:5000/users/${userId}`);

        if (!response.ok) {
          throw new Error("Failed fetching user data.");
        }

        const data = await response.json();
        setUserData(data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchUserData();
  }, [userId]);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!userData) {
    return <div>Loading...</div>;
  }

  const names = userData.name.split(" ");
  const initialValues = {
    firstName: names[0] || "",
    lastName: names[1] || "",
    email: userData.email,
  };

  return (
    <div className="edit-user-form">
      <div className="edit-user-content">
        <h1>Edit User:</h1>
        <Formik
          initialValues={initialValues}
          onSubmit={async (values) => {
            try {
              const response = await fetch(
                `http://127.0.0.1:5000/users/${userId}`,
                {
                  method: "PUT",
                  headers: {
                    "Content-Type": "application/json",
                  },
                  body: JSON.stringify({
                    name: `${values.firstName} ${values.lastName}`,
                    email: values.email,
                    ...(values.password ? { password: values.password } : {}),
                  }),
                }
              );

              if (!response.ok) {
                throw new Error("Update failed.");
              }

              const data = await response.json();

              if (response.status === 200) {
                alert("User updated successfully!");
                // Optionally re-fetch user data
                // fetchUserData();
              } else {
                alert(data.message || "Update failed.");
              }
            } catch (err) {
              alert(err.message);
            }
          }}
        >
          <Form className="form-border">
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
              placeholder="Luna@acme.com"
              type="email"
            />
            <br />
            <label htmlFor="password">
              New Password (leave blank if unchanged)
            </label>
            <br />
            <Field
              id="password"
              name="password"
              placeholder="********"
              type="password"
            />
            <br />
            <Button variant="primary" type="submit" className="form-button">
              Update
            </Button>
            <br />
          </Form>
        </Formik>
      </div>
    </div>
  );
}

export default EditUser;
