from tqdm import tqdm
from . import adb, detect

# install replacement APKs
def install():
	print('[*] Installing')
	chipset = detect.model()

	install = {
		'Launcher': 'com.google.android.apps.nexuslauncher',
		'Equalizer': 'com.android.musicfx',
		'Phone': 'com.google.android.dialer',
		'Overlay_Settings': 'com.android.settings.AOSPifyOverlays.AOSPify',
		'Overlay_SystemUI': 'com.android.systemui.AOSPifyOverlays.AOSPify',
		'Overlay_Android': 'android.AOSPifyOverlays.AOSPify',
		'Overlay_AOD': 'com.samsung.android.app.aodservice.AOSPifyOverlays.AOSPify',
		'Overlay_Font': 'com.monotype.android.font.foundation.AOSPifyOverlays.GoogleProductSans'
	}

	if chipset == detect.DEVICE_EXYNOS:
		install['Camera_exynos'] = 'com.google.android.GoogleCamera'
	elif chipset == detect.DEVICE_SNAPDRAGON:
		install['Camera_snapdragon'] = 'com.google.android.GoogleCamera'

	for apk in tqdm(install, desc='Installing'):
		adb.uninstall(install[apk], keep_data=True)
		adb.install('apk/' + apk + '.apk')
