@echo off
:: Self-elevation script to bypass Windows UIPI for Admin games (e.g. Genshin / Persona 5 with anti-cheat)
net session >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [*] Requesting Administrator privileges to interact with elevated games...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)
cd /d "%~dp0"
call run_yomiflow.bat

