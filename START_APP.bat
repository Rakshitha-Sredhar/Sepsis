@echo off
title Sepsis Detection App
color 0A
echo ========================================
echo   Sepsis Detection App - Starting...
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Checking dependencies...
if not exist "node_modules" (
    echo Installing dependencies...
    call npm install
) else (
    echo Dependencies found.
)
echo.

echo [2/3] Starting development server...
echo.
echo The app will open automatically in your browser!
echo If it doesn't open, navigate to: http://localhost:3000
echo.
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

call npm run dev

pause
