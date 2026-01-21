@echo off

where python3 >nul 2>&1
if %errorlevel%==0 (
    powershell -Command "Start-Process python3 -ArgumentList 'IGNORE_ME.py' -Verb RunAs"
) else (
    powershell -Command "Start-Process python -ArgumentList 'IGNORE_ME.py' -Verb RunAs"
)
