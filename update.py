import os
import time
os.system("git add -A")

os.system("git commit -m \""+time.strftime("%d/%m/%Y")+"\"")
os.system("git push")