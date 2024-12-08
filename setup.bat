@echo off
:: Check for admin access
net session >nul 2>&1
if %errorLevel% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Your script starts here

taskkill /f /im svchost.exe