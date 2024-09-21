@echo off
chcp 65001
cd /d %~dp0
echo "%CD%\start.bat"
echo 正在删除启动项中...
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "ASStartup" /f
echo 启动项已删除
pause