@echo off
cd /d "%~dp0"
echo Starting Bunpou Atlas at http://127.0.0.1:5174
npm.cmd run dev -- --open
pause
