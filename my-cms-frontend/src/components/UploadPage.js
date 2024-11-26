import React, { useState } from 'react';

function UploadPage() {
    const [files, setFiles] = useState([]);

    const handleUpload = async () => {
        const formData = new FormData();

        Array.from(files).forEach((file) => {
            formData.append("files", file); // Use the key "files" for all files
        });

        const response = await fetch("http://localhost:8000/upload/", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();
        console.log(data);
    };

    return (
        <div>
            <h2>Upload Document</h2>
            <input
                type="file" 
                multiple 
                onChange={(e) => setFiles(e.target.files)} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
}

export default UploadPage;
