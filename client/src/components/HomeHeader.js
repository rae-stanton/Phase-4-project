import React from "react";
import Search from "./Search.js";

function HomeHeader({ searchInput, setSearchInput }) {
  return (
    <div>
      {" "}
      <Search searchInput={searchInput} setSearchInput={setSearchInput} />;
    </div>
  );
}

export default HomeHeader;
