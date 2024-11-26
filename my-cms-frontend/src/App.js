import React from 'react';
import UploadPage from './components/UploadPage';
import SearchPage from './components/SearchPage';

function App() {
    return (
        <div>
            <h1>Document Management System</h1>
            <b>
                <p>Hey there! To get started, upload a file and then choose what to do with it...</p>
            </b>
            <UploadPage />
            <SearchPage />
        </div>
    );
}

export default App;
