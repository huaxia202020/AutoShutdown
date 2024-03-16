@echo off
chcp 65001
echo "正在安装python"
python-3.12.2-amd64.exe /quiet PrependPath=1
echo "正在安装python-win11toast"
pip install win11toast
start StartUp.bat
pause
del "python-3.12.2-amd64.exe"
exit