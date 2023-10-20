import React, { useState, useEffect } from "react";
import { Formik, Field, Form } from "formik";
import Button from "react-bootstrap/Button";
import { useParams, useNavigate } from "react-router-dom";
import "./EditUser.css";
import loginImage from "../images/login.png";
import FlashMessage from "./FlashMessage";

function EditUser(props) {
  const { userId } = useParams();
  const navigate = useNavigate();
  const [userData, setUserData] = useState(null);
  const [error, setError] = useState(null);
  const [flash, setFlash] = useState({ visible: false, message: "" });

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

  const deleteUser = async () => {
    if (!window.confirm("Are you sure you want to delete this user?")) return;

    try {
      const response = await fetch(`http://127.0.0.1:5000/users/${userId}`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("Deletion failed.");
      }

      const duration = 3000;
      setFlash({ visible: true, message: "User deleted successfully!" });
      setTimeout(() => {
        navigate("/");
      }, duration);
    } catch (err) {
      setFlash({ visible: true, message: err.message });
    }
  };

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
    <div className="edit-form">
      {flash.visible && <FlashMessage message={flash.message} />}
      <div className="edit-form-content">
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

              const duration = 3000;
              setFlash({
                visible: true,
                message: "User updated successfully!",
              });
              setTimeout(() => {
                navigate("/");
              }, duration);
            } catch (err) {
              setFlash({ visible: true, message: err.message });
            }
          }}
        >
          {() => (
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
              <Button
                variant="danger"
                onClick={deleteUser}
                className="delete-button"
              >
                Delete User
              </Button>
            </Form>
          )}
        </Formik>
      </div>
    </div>
  );
}

export default EditUser;
