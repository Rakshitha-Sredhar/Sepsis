# Sepsis Detection App

A React-based clinical decision support system for sepsis detection using VAE-augmented machine learning.

## Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open your browser and navigate to:
```
http://localhost:3000
```

The server should automatically open in your default browser.

## Troubleshooting

If the app is not displaying:

1. **Check if the server is running:**
   - Look for "Local: http://localhost:3000" in the terminal
   - Try accessing http://localhost:3000 manually

2. **Check browser console:**
   - Press F12 to open developer tools
   - Look for any red error messages in the Console tab

3. **Clear browser cache:**
   - Press Ctrl+Shift+R (or Cmd+Shift+R on Mac) to hard refresh

4. **Check if port 3000 is available:**
   ```bash
   netstat -ano | findstr :3000
   ```

5. **Restart the server:**
   - Stop the current server (Ctrl+C)
   - Run `npm run dev` again

## Features

- User authentication (Login/Signup)
- Patient assessment dashboard
- Sepsis risk analysis
- Model performance comparison charts
- AI-generated clinical recommendations
- Patient records management

## Build for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.






