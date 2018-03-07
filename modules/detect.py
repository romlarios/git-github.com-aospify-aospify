from . import adb

DEVICE_UNKNOWN = 0
DEVICE_EXYNOS = 1
DEVICE_SNAPDRAGON = 2

def get_model():
	name = adb.shell('getprop ro.product.device').strip('\r\n')

	if name in ['dreamqlte', 'dream2qlte']:
		return DEVICE_SNAPDRAGON
	elif name in ['dreamlte', 'dream2lte']:
		return DEVICE_EXYNOS
	else:
		return DEVICE_UNKNOWN
