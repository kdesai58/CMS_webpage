import React, { useState } from 'react';

function UploadPage() {
    const [file, setFile] = useState(null);

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append("file", file);

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
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
}

export default UploadPage;
