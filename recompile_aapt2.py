import os
import sys

args = sys.argv[1:]

# usage `python3 recompile.py APK_FILE`

os.system(f"apktool b -f -d --use-aapt2 RE-{args[0]}")