import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

// Initialize storage mock BEFORE React renders
(function initStorage() {
  if (typeof window !== 'undefined' && !window.storage) {
    window.storage = {
      get: async (key: string) => {
        try {
          const value = localStorage.getItem(key);
          return value ? { value } : null;
        } catch (error) {
          console.error('Storage get error:', error);
          return null;
        }
      },
      set: async (key: string, value: string) => {
        try {
          localStorage.setItem(key, value);
        } catch (error) {
          console.error('Storage set error:', error);
          throw error;
        }
      },
      delete: async (key: string) => {
        try {
          localStorage.removeItem(key);
        } catch (error) {
          console.error('Storage delete error:', error);
        }
      }
    };
  }
})();

const rootElement = document.getElementById('root');
if (!rootElement) {
  console.error('Root element not found!');
  document.body.innerHTML = '<div style="padding: 20px; color: red;">Error: Root element not found. Please check index.html</div>';
} else {
  try {
    ReactDOM.createRoot(rootElement).render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
    );
    console.log('App rendered successfully');
  } catch (error) {
    console.error('Failed to render app:', error);
    rootElement.innerHTML = `<div style="padding: 20px; color: red;">Error rendering app: ${error}</div>`;
  }
}

