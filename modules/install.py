import sys

sys.path.insert(0, 'modules')
import adb

APK_CAMERA = 'apk/Camera.apk'
APK_LAUNCHER = 'apk/Launcher.apk'
APK_PHONE = 'apk/Phone.apk'

# install replacement APKs
def install():
	adb.install(APK_CAMERA)
	adb.install(APK_LAUNCHER)
	adb.install(APK_PHONE)