@echo off
cd /d %~dp0
call app_env\Scripts\activate.bat
if '%ERRORLEVEL%'=='0' (
    start pythonw main.py prod
)

