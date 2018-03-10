from . import adb

LIST_DELETE_GLOBAL = 'assets/delete_global.txt'
LIST_DELETE_SYSTEM = 'assets/delete_system.txt'
LIST_DELETE_SECURE = 'assets/delete_secure.txt'

def settings():
	print('[*] Finishing up')

	# setup overlays first
	adb.enable_overlays('com.android.settings.AOSPifyOverlays.AOSPify',
				'com.android.systemui.AOSPifyOverlays.AOSPify',
				'android.AOSPifyOverlays.AOSPify',
				'com.samsung.android.app.aodservice.AOSPifyOverlays.AOSPify',
				'com.monotype.android.font.foundation.AOSPifyOverlays.GoogleProductSans')

	adb.set_system(double_tab_launch_component='com.google.android.GoogleCamera/com.android.camera.CameraLauncher',
				lock_application_shortcut='null',
				intelligent_sleep_mode=0,
				fingerprint_gesture_quick=1)

	adb.set_secure(sysui_nav_bar='null',
				qs_tile_column=3,
				qs_tile_row=3,
				qs_tile_layout=3,
				sysui_qqs_count=6)

	adb.set_global(navigationbar_key_order=1,
				navigationbar_color=-16777216,
				online_manual_url='https://aospify.github.io/',
				flip_font_style=15,
				dialer_default_application='com.google.android.dialer',
				sms_default_application='com.google.android.apps.messaging')

	with open(LIST_DELETE_GLOBAL, 'r') as f:
		for key in f.readlines():
			adb.shell('settings delete global ' + key)

	with open(LIST_DELETE_SYSTEM, 'r') as f:
		for key in f.readlines():
			adb.shell('settings delete system ' + key)

	with open(LIST_DELETE_SECURE, 'r') as f:
		for key in f.readlines():
			adb.shell('settings delete secure ' + key)
