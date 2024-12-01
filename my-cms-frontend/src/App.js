import React, { useState } from 'react';    // Import the useState hook
import UploadPage from './components/UploadPage';   // Import the UploadPage component
import SearchPage from './components/SearchPage';   // Import the SearchPage component

function App() {    // Define the App component
    const [summaries, setSummaries] = useState([]);  // State to store summaries

    return (    // Render the App component
        <div className="app-container"> {/* Container for the app */}
            <header className="header"> {/* Header section */}
                <h1>Document Management System</h1> {/* Page title */}
            </header>   {/* Close the header tag */}

            <main className="content">  {/* Main content section */}
                <UploadPage setSummaries={setSummaries} />  {/* Render the UploadPage component */}
                <SearchPage />  {/* Render the SearchPage component */}

                {/* Display summaries in the centered box */}
                {summaries.length > 0 && (  // Check if a summary was given, which in all cases will be true as handled by the backend
                    <div className="summary-box">   {/* Centered box */}
                        <h3>Document Summaries:</h3>    {/* Title */}
                        <ul>    {/* Unordered list */}
                            {summaries.map((summary, index) => (    // Iterate over the summaries
                                <li key={index}>    {/* List item */}
                                    <strong>{summary.filename}:</strong> {summary.summary}  {/* Display the filename and summary */}
                                </li>   // Close the list item tag
                            ))}
                        </ul>
                    </div>
                )}
            </main>

            <footer className="footer"> {/* Footer section */}
                <p>&copy; 2024 My CMS App</p>   {/* Footer text */}
            </footer>   {/* Close the footer tag */}
        </div>
    );
}

export default App; // Export the App component
