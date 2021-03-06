from . import adb

LIST_DELETE_GLOBAL = 'assets/delete_global.txt'
LIST_DELETE_SYSTEM = 'assets/delete_system.txt'
LIST_DELETE_SECURE = 'assets/delete_secure.txt'

def settings():
	print('[*] Finishing up')

	# grant perms to BixBack
	adb.shell('pm grant com.draco.bixback android.permission.READ_LOGS')

	# setup overlays first
	adb.enable_overlays('com.android.settings.AOSPifyOverlays.AOSPify',
				'com.android.systemui.AOSPifyOverlays.AOSPify',
				'android.AOSPifyOverlays.AOSPify',
				'com.samsung.android.app.aodservice.AOSPifyOverlays.AOSPify',
				'com.monotype.android.font.foundation.AOSPifyOverlays.GoogleProductSans')

	adb.set_system(double_tab_launch_component='com.google.android.GoogleCamera/com.android.camera.CameraLauncher',
				double_tab_launch=3,
				lock_application_shortcut='null',
				intelligent_sleep_mode=0,
				fingerprint_gesture_quick=1)

	adb.set_secure(qs_tile_column=3,
				qs_tile_row=3,
				qs_tile_layout=3,
				sysui_qqs_count=6)

	adb.set_global(navigationbar_color=-16777216,
				online_manual_url='https://aospify.github.io/',
				flip_font_style=1,
				dialer_default_application='com.google.android.dialer',
				sms_default_application='com.google.android.apps.messaging')

	# ensure BixBack has accessibility perms
	acs_enabled = adb.shell('settings get secure enabled_accessibility_services').strip('\r\n')
	if acs_enabled in ['', 'null']:
		adb.set_secure(enabled_accessibility_services='com.draco.bixback/com.draco.bixback.AccessibilityService')
	elif 'com.draco.bixback.AccessibilityService' not in acs_enabled:
		adb.set_secure(enabled_accessibility_services=acs_enabled + ':com.draco.bixback/com.draco.bixback.AccessibilityService')

	with open(LIST_DELETE_GLOBAL, 'r') as f:
		for key in f.readlines():
			adb.shell('settings delete global ' + key)

	with open(LIST_DELETE_SYSTEM, 'r') as f:
		for key in f.readlines():
			adb.shell('settings delete system ' + key)

	with open(LIST_DELETE_SECURE, 'r') as f:
		for key in f.readlines():
			adb.shell('settings delete secure ' + key)
