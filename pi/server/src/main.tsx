import React from 'react'
import ReactDOM from 'react-dom/client'
import DefaultLayout from './layout/default.tsx';
import App from "./App"

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
)
