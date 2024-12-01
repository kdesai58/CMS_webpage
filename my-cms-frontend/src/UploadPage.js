import React, { useState } from 'react';    // Import the useState hook

function UploadPage() {  // Define the UploadPage component
    const [file, setFile] = useState(null); // Initialize the "file" state

    const handleUpload = async () => {  // Define the handleUpload function
        const formData = new FormData();    // Create a new FormData object
        formData.append("file", file);  // Append the file to the form data

        try {   // Try to upload the file to the backend
            const response = await fetch("http://127.0.0.1:8000/upload/", {     // Fetch the upload endpoint
                method: "POST", // Use the POST method
                body: formData, // Set the request body
            });

            if (response.ok) {  // Check if the response is successful
                const data = await response.json(); // Parse the JSON response
                console.log("File uploaded successfully:", data);   // Debugging
            } else {    // Handle errors
                console.error("Error uploading file:", response);   // Log the error
            }
        } catch (error) {   // Handle network errors
            console.error("Error during upload:", error);   // Log the error
        }
    };

    return (    // Render the UploadPage component
        <div>
            <h2>Upload Document</h2>    {/* Display the page title */}
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />  {/* Display the file input field */}
            <button onClick={handleUpload}>Upload</button>  {/* Display the upload button */}
        </div>  // Close the div tag
    );
}

export default UploadPage;  // Export the UploadPage component
