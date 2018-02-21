import sys

sys.path.insert(0, 'modules')
import adb

_COMM_CAM_DOUBLE_TAP = 'settings put system double_tab_launch_component com.google.android.GoogleCamera/com.android.camera.CameraLauncher'
_COMM_IMMERSIVE_FULL = 'settings put global policy_control "immersive.full=*"'

def setup():
	adb.shell(_COMM_CAM_DOUBLE_TAP)
	adb.shell(_COMM_IMMERSIVE_FULL)