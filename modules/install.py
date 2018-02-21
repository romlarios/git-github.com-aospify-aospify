import sys

sys.path.insert(0, 'modules')
import adb

_APK_CAMERA = 'apk/Camera.apk'
_APK_LAUNCHER = 'apk/Launcher.apk'
_APK_PHONE = 'apk/Phone.apk'

# install replacement APKs
def install():
	adb.install(_APK_CAMERA)
	adb.install(_APK_LAUNCHER)
	adb.install(_APK_PHONE)