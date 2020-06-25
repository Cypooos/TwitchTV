@echo off
del out\TwitchTVwin.exe
call venv\Scripts\activate
venv\Scripts\pyinstaller --onefile --icon="icon.ico" src\vlcscheduler.py
