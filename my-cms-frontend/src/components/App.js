import React from 'react';  // Import the React library
import UploadPage from './components/UploadPage';   // Import the UploadPage component
import SearchPage from './components/SearchPage';   // Import the SearchPage component
import SummaryPage from './components/SummaryPage'; // Import the SummaryPage component

function App() {    // Define the App component
    return (    // Render the App component
        <div>
            <h1>Document Management System</h1> {/* Display the page title */}
            <UploadPage />  {/* Render the UploadPage component */}
            <SearchPage />  {/* Render the SearchPage component */}
            <SummaryPage /> {/* Render the SummaryPage component */}
        </div>  
    );
}

export default App; // Export the App component
