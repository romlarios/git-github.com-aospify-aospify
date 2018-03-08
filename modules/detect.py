import sys
from . import adb

DEVICE_UNCHECKED = -1
DEVICE_UNKNOWN = 0
DEVICE_EXYNOS = 1
DEVICE_SNAPDRAGON = 2

_model = DEVICE_UNCHECKED

def model():
	global _model

	if _model != DEVICE_UNCHECKED:
		return _model

	name = adb.shell('getprop ro.product.device').strip('\r\n')

	if name in ['dreamqlte', 'dream2qlte', 'dreamqltesq', 'dream2qltesq', 'greatqlte', 'greatqltesq']:
		_model = DEVICE_SNAPDRAGON
	elif name in ['dreamlte', 'dream2lte', 'greatlte']:
		_model = DEVICE_EXYNOS
	else:
		_model = DEVICE_UNKNOWN
		choice = input('''UNSUPPORTED DEVICE! Some or all features will not work, and support will not be provided.
Do you wish to continue? (y/n) ''')

		if not choice.startswith('y'):
			print('Aborting.')
			sys.exit()

	return _model
