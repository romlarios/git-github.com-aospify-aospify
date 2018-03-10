from tqdm import tqdm
from . import adb, detect

APK_GCAM_EXYNOS = 'apk/Camera_exynos.apk'
APK_GCAM_SD = 'apk/Camera_snapdragon.apk'
APK_LAUNCHER = 'apk/Launcher.apk'
APK_PHONE = 'apk/Phone.apk'
APK_EQ = 'apk/Equalizer.apk'
APK_OVERLAY_SETTINGS = 'apk/Overlay_Settings.apk'
APK_OVERLAY_SYSTEMUI = 'apk/Overlay_SystemUI.apk'
APK_OVERLAY_ANDROID = 'apk/Overlay_Android.apk'
APK_OVERLAY_AOD = 'apk/Overlay_AOD.apk'
APK_OVERLAY_FONT = 'apk/Overlay_Font.apk'

# install replacement APKs
def install():
	print('[*] Installing apps')
	chipset = detect.model()

	install = {
		APK_LAUNCHER: 'com.google.android.apps.nexuslauncher',
		APK_EQ: 'com.android.musicfx',
		APK_PHONE: 'com.google.android.dialer',
		APK_OVERLAY_SETTINGS: 'com.android.settings.SystemMods.AOSPify',
		APK_OVERLAY_SYSTEMUI: 'com.android.systemui.SystemMods.AOSPify',
		APK_OVERLAY_ANDROID: 'android.SystemMods.AOSPify',
		APK_OVERLAY_AOD: 'com.samsung.android.app.aodservice.SystemMods.AOSPify',
		APK_OVERLAY_FONT: 'com.monotype.android.font.foundation.SystemMods.GoogleProductSans'
	}

	if chipset == detect.DEVICE_EXYNOS:
		install[APK_GCAM_EXYNOS] = 'com.google.android.GoogleCamera'
	elif chipset == detect.DEVICE_SNAPDRAGON:
		install[APK_GCAM_SD] = 'com.google.android.GoogleCamera'

	for apk in tqdm(install, desc='Installing'):
		adb.uninstall(install[apk], keep_data=True)
		adb.install(apk)
