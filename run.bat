@echo off
title YomiFlow Launcher
echo ========================================================
echo    YomiFlow - Universal Japanese Immersion Assistant
echo ========================================================
echo.
echo Starting YomiFlow Overlay...
python -m backend.app
if %errorlevel% neq 0 (
    echo.
    echo YomiFlow exited with error code %errorlevel%.
    pause
)
