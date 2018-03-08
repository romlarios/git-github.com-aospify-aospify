from . import adb

CMD_CAM_DOUBLE_PWR = 'settings put system double_tab_launch_component com.google.android.GoogleCamera/com.android.camera.CameraLauncher'
CMD_NAVBAR_LAYOUT = 'settings put secure sysui_nav_bar "space,back;home;recent,menu_ime"'

def settings():
	adb.shell(CMD_CAM_DOUBLE_PWR)
	adb.shell(CMD_NAVBAR_LAYOUT)
	
