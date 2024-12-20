import React from 'react';  // Import the React library
import ReactDOM from 'react-dom/client';  // Import the ReactDOM library
import './index.css';  // Import the index.css file
import App from './App';  // Import the App component
import reportWebVitals from './reportWebVitals';  // Import the reportWebVitals function

const root = ReactDOM.createRoot(document.getElementById('root'));  // Create a root for the app
root.render(  // Render the app
  <React.StrictMode>  
    {/* Render the App component */}
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
