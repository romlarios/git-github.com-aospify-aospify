from . import adb, detect

APK_GCAM_EXYNOS = 'apk/Camera_exynos.apk'
APK_GCAM_SD = 'apk/Camera_snapdragon.apk'
APK_LAUNCHER = 'apk/Launcher.apk'
APK_PHONE = 'apk/Phone.apk'
APK_EQ = 'apk/Equalizer.apk'
APK_SETTINGS_OVERLAY = 'apk/Settings_overlay.apk'

# install replacement APKs
def install():
	chipset = detect.model()

	if chipset == detect.DEVICE_EXYNOS:
		adb.install(APK_GCAM_EXYNOS)
	elif chipset == detect.DEVICE_SNAPDRAGON:
		adb.install(APK_GCAM_SD)

	adb.install(APK_LAUNCHER)
	adb.install(APK_EQ)
	adb.install(APK_PHONE)

	adb.install(APK_SETTINGS_OVERLAY)
