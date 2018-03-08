from tqdm import tqdm
from . import adb, detect

APK_GCAM_EXYNOS = 'apk/Camera_exynos.apk'
APK_GCAM_SD = 'apk/Camera_snapdragon.apk'
APK_LAUNCHER = 'apk/Launcher.apk'
APK_PHONE = 'apk/Phone.apk'
APK_EQ = 'apk/Equalizer.apk'
APK_OVERLAY_SETTINGS = 'apk/Overlay_Settings.apk'
APK_OVERLAY_SYSTEMUI = 'apk/Overlay_SystemUI.apk'

# install replacement APKs
def install():
	print('[*] Installing apps')
	chipset = detect.model()

	install = [
		APK_LAUNCHER,
		APK_EQ,
		APK_PHONE,
		APK_OVERLAY_SETTINGS,
		APK_OVERLAY_SYSTEMUI
	]

	if chipset == detect.DEVICE_EXYNOS:
		install.append(APK_GCAM_EXYNOS)
	elif chipset == detect.DEVICE_SNAPDRAGON:
		install.append(APK_GCAM_SD)

	for apk in tqdm(install, desc='Installing'):
		adb.install(apk)
