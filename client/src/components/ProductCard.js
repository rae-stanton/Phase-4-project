import React from "react";
import Card from "react-bootstrap/Card";
import "./ProductCard.css";

function ProductCard({ product, onClick }) {
  return (
    <Card className="prod-cards" onClick={onClick}>
      <Card.Img variant="top" src={product.image} className="prod-card-image" />

      <Card.Body>
        <Card.Title>{product.name}</Card.Title>
        <Card.Text>{product.description}</Card.Text>
        <Card.Text>Price: ${product.price}</Card.Text>
        <Card.Text>Amount in Stock: {product.count}</Card.Text>
        <Card.Text>Categories: {product.category}</Card.Text>
      </Card.Body>
    </Card>
  );
}

export default ProductCard;
