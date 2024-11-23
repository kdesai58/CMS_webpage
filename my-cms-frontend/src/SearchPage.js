import React, { useState } from 'react';

function SearchPage() {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        const response = await fetch("http://localhost:8000/search/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query }),
        });

        const data = await response.json();
        setResults(data.results);
    };

    return (
        <div>
            <h2>Search Documents</h2>
            <input type="text" onChange={(e) => setQuery(e.target.value)} />
            <button onClick={handleSearch}>Search</button>
            <ul>
                {results.map((result, idx) => (
                    <li key={idx}>{result.filename}</li>
                ))}
            </ul>
        </div>
    );
}

export default SearchPage;