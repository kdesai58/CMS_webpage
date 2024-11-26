import React, { useState } from 'react';

function UploadPage() {
    const [files, setFiles] = useState([]);
    const [summary, setSummary] = useState(''); // Stores the summary text

    const handleUpload = async () => {
        const formData = new FormData();

        Array.from(files).forEach((file) => {
            formData.append("files", file); // Use the key "files" for all files
        });

        try {
            const response = await fetch("http://localhost:8000/upload/", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            console.log("Upload Response:", data);
        } catch (error) {
            console.error("Error during upload:", error);
        }
    };

    const handleSummarize = async () => {
        if (files.length === 0) {
            alert("Please select a file to summarize!");
            return;
        }

        const formData = new FormData();
        formData.append("file", files[0]); // Use the first file for summarization

        try {
            const response = await fetch("http://localhost:8000/summarize/", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            console.log("Summary Response:", data);
            setSummary(data.summary); // Update summary state with response
        } catch (error) {
            console.error("Error during summarization:", error);
        }
    };

    return (
        <div>
            <h2>Upload and Summarize Document</h2>
            <input
                type="file"
                multiple
                onChange={(e) => setFiles(e.target.files)}
            />
            <button onClick={handleUpload}>Upload</button>
            <button onClick={handleSummarize}>Summarize</button>

            {summary && (
                <div>
                    <h3>Document Summary:</h3>
                    <p>{summary}</p>
                </div>
            )}
        </div>
    );
}

export default UploadPage;
