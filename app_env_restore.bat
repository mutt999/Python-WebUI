@echo off
call app_env\Scripts\activate.bat
if '%ERRORLEVEL%'=='0' (
    pip install -r modules.pip
)


