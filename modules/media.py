from . import adb

MEDIA_DIR = 'assets/media'
MEDIA_DEVICE_UI_DIR = '/data/local/tmp/media_ui'

def _snd(name):
	return f'{MEDIA_DEVICE_UI_DIR}/{name}.ogg'

def media():
	print('[*] Installing sounds')

	adb.push(MEDIA_DIR, '/data/local/tmp/px_media')
	adb.shell('cd /data/local/tmp',
			'rm -rf media_ui /sdcard/{Alarms,Notifications,Ringtones}/AOSPify',
			'mv px_media/alarms /sdcard/Alarms/AOSPify',
			'mv px_media/notifications /sdcard/Notifications/AOSPify',
			'mv px_media/ringtones /sdcard/Ringtones/AOSPify',
			'mv px_media/ui media_ui',
			'rm -rf px_media')

	adb.set_global(car_dock_sound=_snd('Dock'),
				car_undock_sound=_snd('Undock'),
				desk_dock_sound=_snd('Dock'),
				desk_undock_sound=_snd('Undock'),
				lock_sound=_snd('Lock'),
				low_battery_sound=_snd('LowBattery'),
				trusted_sound=_snd('Trusted'),
				unlock_sound=_snd('Unlock'),
				wireless_charging_started_sound=_snd('WirelessChargingStarted'))
