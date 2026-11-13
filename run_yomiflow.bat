@echo off
title YomiFlow Launcher
cd /d "%~dp0"

echo ========================================================
echo   Starting YomiFlow Immersion Assistant (Windows 11)   
echo ========================================================

:: Check if Python MeikiOCR daemon is running on port 8766
netstat -ano | findstr 8766 | findstr LISTENING >nul
if %ERRORLEVEL% NEQ 0 (
    echo [*] Starting MeikiOCR neural server in background...
    start /b python yomiflow_ocr_server.py
    timeout /t 2 /nobreak >nul
) else (
    echo [*] MeikiOCR neural server is already active on port 8766.
)

:: Run release binary if exists, else debug
if exist "target\release\yomiflow.exe" (
    echo [*] Launching optimized release build...
    start "" "target\release\yomiflow.exe"
) else (
    echo [*] Launching debug build...
    start "" "target\debug\yomiflow.exe"
)

echo [*] YomiFlow is active! Press F8 in game to capture dialogue.

