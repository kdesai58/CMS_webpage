import React, { useState } from "react";    // Import the useState hook

function UploadPage() {
    const [files, setFiles] = useState([]); // State to store selected files
    const [summaries, setSummaries] = useState([]); // State to store summaries
    const [response, setResponse] = useState([]); // State to store messages

    const handleUpload = async () => {  // Define the handleUpload function
        const formData = new FormData();    // Create a new FormData object

        Array.from(files).forEach((file) => {   // Iterate over the selected files
            formData.append("files", file); // Match "files" key with backend
        });

        try {   // Try to upload the files to the backend
            const response = await fetch("http://localhost:8000/upload/", {   // Fetch the upload endpoint
                method: "POST", // Use the POST method
                body: formData, // Set the request body
            });

            if(response.ok) {   // Check if the response is successful
            const data = await response.json(); // Parse the JSON response
            console.log("Upload Response:", data);  // Debugging
            setResponse(data.response); // Update state with response
            }
            else{   // Handle errors
                console.error("Error uploading files:", response.status);   // Log the error
            }
        } catch (error) {   // Handle network errors
            console.error("Error during upload:", error);   // Log the error
        }
    };

    const handleSummarize = async () => {   // Define the handleSummarize function
        if (files.length === 0) {   // Check if no files are selected
            alert("Please select at least one file to summarize!");  // Show an alert to the user
            return; // Exit the function early
        }

        const formData = new FormData();    // Create a new FormData object
        Array.from(files).forEach((file) => {   // Iterate over the selected files
            formData.append("files", file); // Match "files" key with backend
        });

        try {   // Try to summarize the files on the backend
            const response = await fetch("http://localhost:8000/summary/summarize/", {  // Fetch the summarize endpoint
                method: "POST", // Use the POST method
                body: formData, // Set the request body
            });

            if (response.ok) {  // Check if the response is successful
                const data = await response.json(); // Parse the JSON response
                console.log("Summary Response:", data); // Debugging
                setSummaries(data.summaries); // Update state with summaries
            } else {    // Handle errors
                console.error("Error summarizing files:", response.status); // Log the error
            }   
        } catch (error) {   // Handle network errors
            console.error("Error during summarize request:", error);    // Log the error
        }
    };

    return (    // Render the UploadPage component
        <div className="content-container" >    {/* Container for the upload form */}
            <h2>Upload and Summarize Documents</h2>   {/* Display the page title */}
            <input  // Display the file input field
                type="file" // Set the input type
                multiple    // Allow multiple file selection
                onChange={(e) => setFiles(e.target.files)}  // Update the "files" state
            />
            <button onClick={handleUpload}>Upload</button>  {/* Display the upload button */}
            <button onClick={handleSummarize}>Summarize</button>    {/* Display the summarize button */}

            {/* Display response messages */}   
            {response.length > 0 && (   // Check if there are response messages
                <div className="response">  {/* Display the response messages */}
                    <h3>Response:</h3>  {/* Display the response title */}
                    <ul>    {/* Display the response list */}
                        {response.map((message, index) => (  // Iterate over the response messages
                            <li key={index}>{message.filename} : {message.message}</li> 
                        ))}
                    </ul>
                </div>
            )}

            {/* Display summaries */}
            {summaries.length > 0 && (  // Check if there are summaries
                <div className="summaries">   {/* Display the summaries */}
                    <h3>Summaries:</h3>   {/* Display the summaries title */}
                    <ul>
                        {summaries.map((summary, index) => (    // Iterate over the summaries
                            <li key={index}>    {/* Display each summary */}
                                <strong>{summary.filename}:</strong> {summary.summary}  {/* Display the filename and summary */}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default UploadPage;  // Export the UploadPage component