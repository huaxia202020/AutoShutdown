@echo off
chcp 65001
echo 正在删除启动项中...
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "ASStaetup" /f
echo 启动项已删除
pause