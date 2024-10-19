import os
os.system("start /wait python.exe ./main.py")
while True:
    if os.path.exists("./Running.lock"):
        os.system("start /wait python.exe ./main.py")
    else:
        exit(0)