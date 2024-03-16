@echo off
chcp 65001
cd /d %~dp0
echo 设置启动项中...
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "ASStaetup" /t REG_SZ /d "%CD%\start.bat" /f
echo 启动项已设置完成