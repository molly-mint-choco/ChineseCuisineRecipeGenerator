import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Optional: Include global styles if needed
import App from './App'; // Import the App component

// Render the App component inside the #root element
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
