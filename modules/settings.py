from . import adb

CMD_CAM_DOUBLE_PWR = 'settings put system double_tab_launch_component com.google.android.GoogleCamera/com.android.camera.CameraLauncher'
CMD_NAVBAR_LAYOUT = 'settings put global navigationbar_key_order 1'
CMD_ENABLE_OVERLAY_SETTINGS = 'cmd overlay enable com.android.settings.SystemMods.AOSPify'
CMD_ENABLE_OVERLAY_SYSTEMUI = 'cmd overlay enable com.android.systemui.SystemMods.AOSPify'
CMD_QS_COLUMNS = 'settings put secure qs_tile_column 3'
CMD_QS_ROWS = 'settings put secure qs_tile_row 3'
CMD_QS_LAYOUT = 'settings put secure qs_tile_layout 3'
CMD_QS_QQS = 'settings put secure sysui_qqs_count 6'

def settings():
	# setup overlays first
	adb.shell(CMD_ENABLE_OVERLAY_SETTINGS)
	adb.shell(CMD_ENABLE_OVERLAY_SYSTEMUI)
	
	adb.shell(CMD_CAM_DOUBLE_PWR)
	adb.shell(CMD_NAVBAR_LAYOUT)
	adb.shell(CMD_QS_COLUMNS)
	adb.shell(CMD_QS_ROWS)
	adb.shell(CMD_QS_LAYOUT)
	adb.shell(CMD_QS_QQS)
	
