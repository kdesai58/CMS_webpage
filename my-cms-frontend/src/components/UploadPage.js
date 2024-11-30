import React, { useState } from "react";

function UploadPage() {
    const [files, setFiles] = useState([]); // State to store selected files
    const [summaries, setSummaries] = useState([]); // State to store summaries
    const [response, setResponse] = useState([]); // State to store messages

    const handleUpload = async () => {
        const formData = new FormData();

        Array.from(files).forEach((file) => {
            formData.append("files", file); // Match "files" key with backend
        });

        try {
            const response = await fetch("http://localhost:8000/upload/", {
                method: "POST",
                body: formData,
            });

            if(response.ok) {
            const data = await response.json();
            console.log("Upload Response:", data);
            setResponse(data.response); // Update state with response
            }
            else{
                console.error("Error uploading files:", response.status);
            }
        } catch (error) {
            console.error("Error during upload:", error);
        }
    };

    const handleSummarize = async () => {
        if (files.length === 0) {
            alert("Please select at least one file to summarize!");
            return;
        }

        const formData = new FormData();
        Array.from(files).forEach((file) => {
            formData.append("files", file); // Match "files" key with backend
        });

        try {
            const response = await fetch("http://localhost:8000/summary/summarize/", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                console.log("Summary Response:", data);
                setSummaries(data.summaries); // Update state with summaries
            } else {
                console.error("Error summarizing files:", response.status);
            }
        } catch (error) {
            console.error("Error during summarize request:", error);
        }
    };

    return (
        <div>
            <h2>Upload and Summarize Documents</h2>
            <input
                type="file"
                multiple
                onChange={(e) => setFiles(e.target.files)}
            />
            <button onClick={handleUpload}>Upload</button>
            <button onClick={handleSummarize}>Summarize</button>

            {/* Display response messages */}
            {response.length > 0 && (
                <div>
                    <h3>Response:</h3>
                    <ul>
                        {response.map((message, index) => (
<<<<<<< HEAD
                            <li key={index}>{message.message}</li>
=======
                            <li key={index}>{message.filename} : {message.message}</li>
>>>>>>> 7036c5dc0d169867ad63743dfdc5dd85b3f83d49
                        ))}
                    </ul>
                </div>
            )}

            {/* Display summaries */}
            {summaries.length > 0 && (
                <div>
                    <h3>Summaries:</h3>
                    <ul>
                        {summaries.map((summary, index) => (
                            <li key={index}>
                                <strong>{summary.filename}:</strong> {summary.summary}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default UploadPage;