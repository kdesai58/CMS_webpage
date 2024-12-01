import React, { useState } from 'react';        // Import the useState hook

function SearchPage() { // Define the SearchPage component
    const [query, setQuery] = useState(''); // Initialize the "query" state
    const [results, setResults] = useState([]); // Initialize the "results" state
    const [error, setError] = useState(''); // Initialize the "error" state

    const handleSearch = async () => {  // Define the handleSearch function
        console.log("Search query:", query); // Debugging
        if (!query.trim()) {    // Check if the query is empty
            alert("Please enter a search query!");  // Show an alert to the user
            return; // Exit the function early
        }
    
        try {   // Try to fetch search results from the backend
            
            const response = await fetch(`http://127.0.0.1:8000/search/`, {  // Fetch from the search endpoint
                method: 'POST', // Use the POST method
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded', // Form data format    
            },
            body: new URLSearchParams({ query }).toString(),    // Set the request body
            });
    
            if (response.ok) {  // Check if the response is successful
                const data = await response.json(); // Parse the JSON response
                console.log("Backend Response:", data); // Debugging
                setResults(data.results || []); // Extract the "results" array
                setError(''); // Clear previous errors
            } else {
                console.error("Search failed:", response.status);   // Log the error
                setError("Failed to fetch search results.");    // Set an error message
            }
        } catch (error) {   // Handle network errors
            console.error("Error during search:", error);   // Log the error
            setError("An error occurred while fetching search results.");   // Set an error message
        }
    };
    

    return (    // Render the SearchPage component
        <div>
            <h2>Search Documents</h2>   {/* Display the page title */}
            <input  // Display the search input field
                type="text"     // Set the input type
                value={query}   // Bind the input value to the "query" state
                onChange={(e) => setQuery(e.target.value)}  // Update the "query" state
                placeholder="Enter search query"    // Set the input placeholder
            />
            <button
                onClick={() => {    // Add a click event handler
                    console.log("Search button clicked!"); // Debugging
                    handleSearch(); // Call the handleSearch function
                }}
            >
            Search  {/* Display the button text */}
            </button>   

            {/* Display error */}
            {error && <p style={{ color: 'red' }}>{error}</p>}  

            {/* Display results */}
            <div>
                <h3>Search Results</h3>  {/* Display the results title */}
                {results.length > 0 ? (  // Check if there are results
                    <ul>    {/* Display the results list */}
                        {results.map((result) => (  // Iterate over the results
                            <li key={result.id}>    {/* Display each result */}
                                <strong>Filename:</strong> {result.filename}    {/* Display the filename */}
                            </li>   // Close the list item tag
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
