import React, { useState } from 'react';

function SearchPage() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState('');
    const [topK] = useState(3);  // Add state for top_k

    const handleSearch = async () => {
        if (!query.trim()) {
            alert("Please enter a search query!");
            return;
        }
    
        try {
            // Updated to use the query parameter name 'query' as defined in FastAPI
            const response = await fetch(`http://127.0.0.1:8000/search/?query=${encodeURIComponent(query)}&top_k=${topK}`, {
                method: 'GET', // Make sure the method is GET
            });
            console.log("Response:", response);
    
            if (response.ok) {
                const data = await response.json();
                console.log("Backend Response:", data);
                setResults(data.results || []);
                setError('');
            } else {
                console.error("Search failed:", response.status);
                setError(`Error: ${response.status} - ${response.statusText}`);
            }
        } catch (error) {
            console.error("Error during search:", error);
            setError("An error occurred while fetching search results.");
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
            {/* Optional input to allow user to set top_k */}
            {/* <input
                type="number"
                value={topK}
                onChange={(e) => setTopK(Number(e.target.value))}
                min="1"
                placeholder="Top K Results"
            /> */}
            <button
                onClick={() => {
                    console.log("Search button clicked!"); // Debugging
                    handleSearch();
                }}
            >
                Search
            </button>

            {/* Display error */}
            {error && <p style={{ color: 'red' }}>{error}</p>}

            {/* Display results */}
            <div>
                <h3>Search Results</h3>
                {results.length > 0 ? (
                    <ul>
                        {results.map((result) => (
                            <li key={result.id}>
                                <strong>Filename:</strong> {result.filename}
                            </li>
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
