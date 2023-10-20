import React from "react";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import "./RecipeDisplay.css";
import ordersImage from "../images/orders.png"; // <-- Import the image here
import ProductList from "./ProductList.js";

function ProductDisplay({ product, onClose }) {
  return (
    <div>
      <h1>Welcome! Here's your info:</h1>
      <DashCardGrid1 />
    </div>
  );
}

function DashCardGrid1() {
  return (
    <div className="card-container">
      <Row xs={1} md={3} className="g-3">
        {Array.from({ length: 3 }).map((_, idx) => (
          <Col key={idx}>
            <Card className="dash-cards">
              <Card.Img
                variant="top"
                src={ordersImage}
                className="dash-card-image"
              />

              <Card.Body>
                <Card.Title>Check this out:</Card.Title>
                <Card.Text>
                  This is whatever thing you will want to find.
                </Card.Text>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default Dashboard;
