import os

with open("./Running.lock", "w") as f:
    pass
while True:
    if os.path.exists("./Running.lock"):
        os.system("python main.py")
    else:
        exit(0)
