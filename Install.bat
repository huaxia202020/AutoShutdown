@echo off
chcp 65001
echo "正在安装python"
python-3.12.2-amd64.exe /quiet PrependPath=1
start StartUp.bat
start pip-install.bat
pause
del "python-3.12.2-amd64.exe"
exit