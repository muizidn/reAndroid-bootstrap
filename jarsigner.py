import os
import sys

args = sys.argv[1:]

# usage `python3 jarsigner.py APK_FILE`

os.system(f"jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore keystore/my-release-key.keystore RE-{args[0]}/dist/{args[0]} alias_name")