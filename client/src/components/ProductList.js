import React, { useState, useEffect } from "react";
import ProductCard from "./ProductCard.js";
import NewProductForm from "./NewProductForm.js";
import ProductDisplay from "./ProductDisplay.js";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import "./ProductList.css";

function ProductList({ searchInput }) {
  const [products, setProducts] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/Products")
      .then((response) => response.json())
      .then(setProducts)
      .catch((error) => console.error("Error fetching products:", error));
  }, []);

  const searchWords = searchInput.toLowerCase().split(" ");
  const searchedProducts = Array.isArray(products)
    ? products.filter((product) => {
        return searchWords.every((word) => {
          const searchTerm = word.trim();
          return product.name.toLowerCase().includes(searchTerm);
          // || (product.category &&
          //   product.category.some((category) =>
          //     category.toLowerCase().includes(searchTerm)
          //   ))
        });
      })
    : [];

  const handleProductClick = (product) => {
    setSelectedProduct(product);
  };

  const handleProductSubmit = (newProduct) => {
    setProducts([...products, newProduct]);
  };

  return (
    <div>
      <ProdCardGrid1
        products={searchedProducts}
        handleProductClick={handleProductClick}
      />
    </div>
  );
}

function ProdCardGrid1({ products, handleProductClick }) {
  return (
    <div className="card-container">
      <Row xs={1} md={3} className="g-3">
        {Array.from({ length: 3 }).map((_, idx) => (
          <Col key={idx} className="my-3">
            {products && products.length > 0 ? (
              products.map((product) => (
                <ProductCard
                  key={product.id}
                  product={product}
                  onClick={() => handleProductClick(product)}
                />
              ))
            ) : (
              <div>No products found.</div>
            )}
          </Col>
        ))}
      </Row>
    </div>
  );
}

// function ProdCardGrid1({ products, handleProductClick }) {
//   return (
//     <div className="card-container">
//       {products && products.length > 0 ? (
//         products.map((product) => (
//           <Col key={product.id} xs={12} sm={6} md={4}>
//             <ProductCard
//               product={product}
//               onClick={() => handleProductClick(product)}
//               className="product-card"
//               key={product.id}
//             />
//           </Col>
//         ))
//       ) : (
//         <div>No products found.</div>
//       )}
//     </div>
//   );
// }

export default ProductList;
