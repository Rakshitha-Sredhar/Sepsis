# Quick Start Guide

## 🚀 Starting the Application

### Option 1: Using npm (Recommended)
```bash
npm run dev
```

### Option 2: Using the batch file (Windows)
Double-click `START_SERVER.bat`

## 🌐 Access the Application

Once the server starts, open your browser and navigate to:

**http://localhost:3000**

## ✅ What You Should See

1. **Loading Screen** - Brief loading animation
2. **Login/Signup Page** - Authentication interface
3. **Dashboard** - After logging in, you'll see the patient assessment dashboard

## 🔧 Troubleshooting

### If you see a blank page:

1. **Open Browser Developer Tools** (Press F12)
2. **Check the Console tab** for any red error messages
3. **Check the Network tab** to see if files are loading

### Common Issues:

- **Port 3000 already in use**: 
  - Stop other applications using port 3000
  - Or change the port in `vite.config.ts`

- **Module not found errors**:
  ```bash
  npm install
  ```

- **TypeScript errors**:
  ```bash
  npx tsc --noEmit
  ```

## 📝 First Time Setup

If this is your first time running the project:

```bash
npm install
npm run dev
```

## 🎯 Testing the App

1. Click "Sign Up" on the login page
2. Enter any email and password
3. Click "Create Account"
4. You'll be taken to the dashboard
5. Fill in patient information and vitals
6. Click "Analyze" to see results

## 📞 Need Help?

Check the browser console (F12) for detailed error messages.






