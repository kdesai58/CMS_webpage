import React, { useState } from 'react';    // Import the useState hook

function UploadPage() { // Define the UploadPage component
    const [file, setFile] = useState(null); // Initialize the "file" state

    const handleUpload = async () => {  // Define the handleUpload function
        const formData = new FormData();    // Create a new FormData object
        formData.append("file", file);  // Append the file to the form data

        const response = await fetch("http://localhost:8000/upload/", { // Fetch the upload endpoint
            method: "POST", // Use the POST method
            body: formData, // Set the request body
        });

        const data = await response.json(); // Parse the JSON response
        console.log(data);  // Log the response data
    };

    return (    // Render the UploadPage component
        <div>   {/* Container for the upload form */}
            <h2>Upload Document</h2>    {/* Display the page title */}
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />  {/* Display the file input field */}
            <button onClick={handleUpload}>Upload</button>  {/* Display the upload button */}
        </div>
    );
}