import os
import sys
import subprocess

def install():
    files = os.listdir('.')

    if 'requirements.txt' in files:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    else:
        print("There is no requirements.txt in the current directory!")