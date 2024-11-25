import React, { useState } from 'react';

function UploadPage() {
    const [file, setFile] = useState(null);

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch("http://127.0.0.1:8000/upload/", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                console.log("File uploaded successfully:", data);
            } else {
                console.error("Error uploading file:", response);
            }
        } catch (error) {
            console.error("Error during upload:", error);
        }
    };

    return (
        <div>
            <h2>Upload Document</h2>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
}

export default UploadPage;
