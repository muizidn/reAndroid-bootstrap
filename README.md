# Lets Reverse Engineer Android APK

https://medium.com/@sandeepcirusanagunla/decompile-and-recompile-an-android-apk-using-apktool-3d84c2055a82

See [Keystore Readme](keystore/README.md)

# Requirements

```
brew install apktool
```

# Try Me!!
```
# provide app.apk in root directory
APKFILE_CLI=app.apk make all
```

Got from Reversing.ID telegram

https://github.com/shroudedcode/apk-mitm

# Readmore!

- https://www.securify.nl/en/blog/android-adb-reverse-tethering-mitm-setup


# PROXY
- https://github.com/theappbusiness/android-proxy-toggle

adb shell settings put global http_proxy 192.168.1.9:9090

adb shell settings delete global http_proxy
adb shell settings delete global global_http_proxy_host
adb shell settings delete global global_http_proxy_port

