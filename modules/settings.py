from . import adb

AOSPIFY_MEDIA_DIR = 'assets/AOSPify_Media'
AOSPIFY_MEDIA_DEVICE_DIR = '/sdcard/AOSPify_Media'
LIST_DELETE_GLOBAL = 'assets/delete_global.txt'
LIST_DELETE_SYSTEM = 'assets/delete_system.txt'
LIST_DELETE_SECURE = 'assets/delete_secure.txt'

def settings():
	print('[*] Finishing up')
	
	adb.push(AOSPIFY_MEDIA_DIR, AOSPIFY_MEDIA_DEVICE_DIR)

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
				flip_font_style=1,
				dialer_default_application='com.google.android.dialer',
				sms_default_application='com.google.android.apps.messaging',
				car_dock_sound=AOSPIFY_MEDIA_DEVICE_DIR + '/ui/Dock.ogg',
				car_undock_sound=AOSPIFY_MEDIA_DEVICE_DIR + '/ui/Undock.ogg',
				desk_dock_sound=AOSPIFY_MEDIA_DEVICE_DIR + '/ui/Dock.ogg',
				desk_undock_sound=AOSPIFY_MEDIA_DEVICE_DIR + '/ui/Undock.ogg',
				lock_sound=AOSPIFY_MEDIA_DEVICE_DIR + '/ui/Lock.ogg',
				low_battery_sound=AOSPIFY_MEDIA_DEVICE_DIR + '/ui/LowBattery.ogg',
				trusted_sound=AOSPIFY_MEDIA_DEVICE_DIR + '/ui/Trusted.ogg',
				unlock_sound=AOSPIFY_MEDIA_DEVICE_DIR + '/ui/Unlock.ogg',
				wireless_charging_started_sound=AOSPIFY_MEDIA_DEVICE_DIR + '/ui/WirelessChargingStarted.ogg')

	with open(LIST_DELETE_GLOBAL, 'r') as f:
		for key in f.readlines():
			adb.shell('settings delete global ' + key)

	with open(LIST_DELETE_SYSTEM, 'r') as f:
		for key in f.readlines():
			adb.shell('settings delete system ' + key)

	with open(LIST_DELETE_SECURE, 'r') as f:
		for key in f.readlines():
			adb.shell('settings delete secure ' + key)
