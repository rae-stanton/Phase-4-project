import React from "react";
import Card from "react-bootstrap/Card";

function ProductCard({ product }) {
  return (
    <Card className="prod-cards">
      <Card.Img variant="top" src={product.image} className="prod-card-image" />

      <Card.Body>
        <Card.Title>{product.name}</Card.Title>
        <Card.Text>{product.description}</Card.Text>
        <Card.Text>Price: ${product.price}</Card.Text>
        <Card.Text>Availability: {product.count} available</Card.Text>
      </Card.Body>
    </Card>
  );
}

export default ProductCard;
