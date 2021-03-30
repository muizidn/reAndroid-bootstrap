import os
import sys

args = sys.argv[1:]

# usage `python3 verify.py APK_FILE`

os.system(f"jarsigner -verify -verbose -certs RE-{args[0]}/dist/{args[0]}")