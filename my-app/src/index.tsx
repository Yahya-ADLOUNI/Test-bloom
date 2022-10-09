import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';

const rootElement = document.getElementById('root');
rootElement?.classList.add("bg-light");
const root = ReactDOM.createRoot(
  rootElement as HTMLElement,
);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);