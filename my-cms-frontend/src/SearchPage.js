import React, { useState } from 'react';

function SearchPage() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/search/?query=${query}`, {
                method: 'GET',
            });

            if (response.ok) {
                const data = await response.json();
                setResults(data);
            } else {
                console.error("Search failed:", response);
            }
        } catch (error) {
            console.error("Error during search:", error);
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
                <h3>Search Results</h3>
                {results.length > 0 ? (
                    <ul>
                        {results.map((result, index) => (
                            <li key={index}>{result.title}</li>
                        ))}
                    </ul>
                ) : (
                    <p>No results found.</p>
                )}
            </div>
        </div>
    );
}

export default SearchPage;
