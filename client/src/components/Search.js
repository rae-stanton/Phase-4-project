import React from "react";

function Search({ searchInput, setSearchInput }) {
  const handleOnChange = (e) => {
    setSearchInput(e.target.value);
  };
  return (
    <div>
      <form className="app-form">
        <div className="input-group mb-3">
          <label className="form-label" htmlFor="searchBar"></label>
          <input
            id="searchBar"
            className="form-control form-control-lg"
            value={searchInput}
            type="text"
            placeholder="Search Product Names..."
            onChange={handleOnChange}
          />
        </div>
      </form>
    </div>
  );
}

export default Search;
