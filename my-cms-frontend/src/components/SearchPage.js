import React, { useState } from 'react';    // Import the useState hook

function SearchPage() { // Define the SearchPage component
    const [query, setQuery] = useState(''); // Initialize the "query" state
    const [results, setResults] = useState([]); // Initialize the "results" state
    const [error, setError] = useState(''); // Initialize the "error" state
    const [topK] = useState(3);  // Add state for top_k results     

    const handleSearch = async () => {
        if (!query.trim()) {    // Check if the query is empty
            alert("Please enter a search query!");  // Show an alert to the user
            return;
        }
    
        try {   // Try to fetch search results from the backend
            // Updated to use the query parameter name 'query' as defined in FastAPI
            const response = await fetch(`http://127.0.0.1:8000/search/?query=${encodeURIComponent(query)}&top_k=${topK}`, {    // Fetch from the search endpoint
                method: 'GET', // method is GET
            });
            console.log("Response:", response); // Debugging
    
            if (response.ok) {  // Check if the response is successful
                const data = await response.json(); // Parse the JSON response
                console.log("Backend Response:", data); // Debugging
                setResults(data.results || []); // Extract the "results" array
                setError('');   // Clear previous errors
            } else {
                console.error("Search failed:", response.status);   // Log the error
                setError(`Error: ${response.status} - ${response.statusText}`);   // Set an error message
            }
        } catch (error) {   // Handle network errors
            console.error("Error during search:", error);   // Log the error
            setError("An error occurred while fetching search results.");   // Set an error message
        }
    };

    return (    // Render the SearchPage component
        <div>   
            <h2>Search Documents</h2>   {/* Display the page title */}
            <input  
                type="text" // Set the input type
                value={query}   // Bind the input value to the "query" state
                onChange={(e) => setQuery(e.target.value)}  // Update the "query" state
                placeholder="Enter search query"    //  Set the input placeholder
            />
            {/* Optional input to allow user to set top_k */}
            {/* <input
                type="number"
                value={topK}
                onChange={(e) => setTopK(Number(e.target.value))}
                min="1"
                placeholder="Top K Results"
            /> */}
            <button // Display the search button
                onClick={() => {    // Add a click event handler
                    console.log("Search button clicked!"); // Debugging
                    handleSearch(); // Call the handleSearch function
                }}
            >
                Search  {/* Display the button text */}
            </button>   

            {/* Display error */}
            {error && <p style={{ color: 'red' }}>{error}</p>}  {/* Display the error message */}

            {/* Display results */}
            <div>
                <h3>Search Results</h3>  {/* Display the results title */}
                {results.length > 0 ? ( // Check if there are results
                    <ul>
                        {results.map((result) => (  // Iterate over the results
                            <li key={result.id}>    {/* Display each result */}
                                <strong>Filename:</strong> {result.filename}    {/* Display the filename */}
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p>No results found.</p>    // Display a message if no results are found
                )}
            </div>
        </div>
    );
}

export default SearchPage;  // Export the SearchPage component
