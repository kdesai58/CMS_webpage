import React from 'react';
import UploadPage from './components/UploadPage';
import SearchPage from './components/SearchPage';
import SummaryPage from './components/SummaryPage';

function App() {
    return (
        <div>
            <h1>Document Management System</h1>
            <UploadPage />
            <SearchPage />
            <SummaryPage />
        </div>
    );
}

export default App;
