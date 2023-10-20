import React, { useState } from "react";
import HomeHeader from "./HomeHeader.js";
import ProductList from "./ProductList.js";
import "./Home.css";

function Home() {
  const [searchInput, setSearchInput] = useState("");
  return (
    <div>
      <HomeHeader searchInput={searchInput} setSearchInput={setSearchInput} />
      <ProductList searchInput={searchInput} />
    </div>
  );
}

export default Home;
