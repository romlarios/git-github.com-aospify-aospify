from . import adb

CMD_ENABLE_OVERLAY_SETTINGS = 'cmd overlay enable com.android.settings.SystemMods.AOSPify'
CMD_ENABLE_OVERLAY_SYSTEMUI = 'cmd overlay enable com.android.systemui.SystemMods.AOSPify'
CMD_ENABLE_OVERLAY_ANDROID = 'cmd overlay enable android.SystemMods.AOSPify'
CMD_ENABLE_OVERLAY_AOD = 'cmd overlay enable com.samsung.android.app.aodservice.SystemMods.AOSPify'

CMD_CAM_DOUBLE_PWR = 'settings put system double_tab_launch_component com.google.android.GoogleCamera/com.android.camera.CameraLauncher'
CMD_NAVBAR_RESET = 'settings put secure sysui_nav_bar null'
CMD_NAVBAR_LAYOUT = 'settings put global navigationbar_key_order 1'
CMD_QS_COLUMNS = 'settings put secure qs_tile_column 3'
CMD_QS_ROWS = 'settings put secure qs_tile_row 3'
CMD_QS_LAYOUT = 'settings put secure qs_tile_layout 3'
CMD_QS_QQS = 'settings put secure sysui_qqs_count 6'
CMD_LOCK_SHORTCUTS = 'settings put system lock_application_shortcut null'
CMD_BLACK_NAV = 'settings put global navigationbar_color -16777216'
CMD_HELP_URL = 'settings put global online_manual_url https://github.com/tytydraco/AOSPify'
CMD_DISABLE_INTELLIGENT_SLEEP = 'settings put system intelligent_sleep_mode 0'
CMD_ENABLE_FINGER_GESTURES = 'settings put system fingerprint_gesture_quick 1'

def settings():
	print('[*] Finishing up')
	# setup overlays first
	adb.shell(CMD_ENABLE_OVERLAY_SETTINGS)
	adb.shell(CMD_ENABLE_OVERLAY_SYSTEMUI)
	adb.shell(CMD_ENABLE_OVERLAY_ANDROID)
	adb.shell(CMD_ENABLE_OVERLAY_AOD)
	
	adb.shell(CMD_CAM_DOUBLE_PWR)
	adb.shell(CMD_NAVBAR_RESET)
	adb.shell(CMD_NAVBAR_LAYOUT)
	adb.shell(CMD_QS_COLUMNS)
	adb.shell(CMD_QS_ROWS)
	adb.shell(CMD_QS_LAYOUT)
	adb.shell(CMD_QS_QQS)
	adb.shell(CMD_LOCK_SHORTCUTS)
	adb.shell(CMD_BLACK_NAV)
	adb.shell(CMD_HELP_URL)
	adb.shell(CMD_DISABLE_INTELLIGENT_SLEEP)
	adb.shell(CMD_ENABLE_FINGER_GESTURES)
