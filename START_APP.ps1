Write-Host "Starting Sepsis Detection App..." -ForegroundColor Green
Write-Host ""
Set-Location $PSScriptRoot

Write-Host "Installing dependencies if needed..." -ForegroundColor Yellow
npm install

Write-Host ""
Write-Host "Starting development server..." -ForegroundColor Yellow
Write-Host "The app will open automatically in your browser at http://localhost:3000" -ForegroundColor Cyan
Write-Host ""

npm run dev




