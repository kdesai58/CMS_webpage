import React, { useState, useEffect } from 'react';

function SearchPage() {
    const [results, setResults] = useState([]); // Initialize as an empty array
    const [query, setQuery] = useState('');

    const handleSearch = async () => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/search?q=${query}`, {
                method: 'GET',
            });
            const data = await response.json();
            setResults(data); // Assuming `data` is an array
        } catch (error) {
            console.error('Error fetching search results:', error);
            setResults([]); // Set to empty array on error
        }
    };

    return (
        <div>
            <h2>Search Documents</h2>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter search query"
            />
            <button onClick={handleSearch}>Search</button>
            <div>
                {results && results.length > 0 ? ( // Conditional rendering
                    results.map((result, index) => (
                        <div key={index}>
                            <p>{result.title}</p>
                            <a href={result.url} target="_blank" rel="noopener noreferrer">
                                Open Document
                            </a>
                        </div>
                    ))
                ) : (
                    <p>No results found</p>
                )}
            </div>
        </div>
    );
}

export default SearchPage;
