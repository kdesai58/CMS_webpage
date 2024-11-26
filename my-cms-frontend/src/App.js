import React, { useState } from 'react';
import UploadPage from './components/UploadPage';
import SearchPage from './components/SearchPage';

function App() {
    const [summaries, setSummaries] = useState([]);  // State to store summaries

    return (
        <div className="app-container">
            <header className="header">
                <h1>Document Management System</h1>
            </header>

            <main className="content">
                <UploadPage setSummaries={setSummaries} />  {/* Passing setSummaries to UploadPage */}
                <SearchPage />

                {/* Display summaries directly below the UploadPage */}
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
            </main>

            <footer className="footer">
                <p>&copy; 2024 My CMS App</p>
            </footer>
        </div>
    );
}

export default App;
