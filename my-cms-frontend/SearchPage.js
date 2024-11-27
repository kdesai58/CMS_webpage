import React, { useState } from 'react';

function SearchPage() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState('');

    const handleSearch = async () => {
        console.log("Search query:", query); // Debugging
        if (!query.trim()) {
            alert("Please enter a search query!");
            return;
        }
    
        try {
            
            const response = await fetch(`http://127.0.0.1:8000/search/`, {
                method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded', // Form data format
            },
            body: new URLSearchParams({ query }).toString(),
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log("Backend Response:", data); // Debugging
                setResults(data.results || []); // Extract the "results" array
                setError(''); // Clear previous errors
            } else {
                console.error("Search failed:", response.status);
                setError("Failed to fetch search results.");
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
