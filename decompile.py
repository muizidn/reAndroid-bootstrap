import os
import sys

args = sys.argv[1:]

# usage `python3 decompile.py APK_FILE`

os.system(f"apktool d -s {args[0]} -o RE-{args[0]}")