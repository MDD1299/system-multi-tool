@echo off
rem Adjust the sound volume (0-100)
powershell -Command "(New-Object -ComObject WScript.Shell).SendKeys([char]175)"