@echo off
chcp 65001
powershell curl -o "python-3.12.2-amd64.exe" "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
echo "正在安装python"
python-3.12.2-amd64.exe /quiet PrependPath=1
echo "正在安装python-win11toast"
pip install win11toast
cd /d %~dp0
echo 设置启动项中...
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "ASStaetup" /t REG_SZ /d "%CD%\start.bat" /f
echo 启动项已设置完成
pause