import os
import sys
import subprocess

ADB_PATH = os.path.abspath('bin/' + sys.platform + '/adb')
if sys.platform == 'win32':
	ADB_PATH += '.exe'

# handle bin missing; call from main.py
def adb_check():
	if not os.path.isfile(ADB_PATH):
		print('[!] ADB binary not found. Abort.')
		sys.exit(1)
	print('[*] ADB check passed')

def device_check():
	devices = exe('devices')

	if 'unauthorized' in devices:
		print('[!] Device unauthorized, please unlock the device and tap OK. Abort.')
		sys.exit(1)
	elif 'recovery' in devices:
		print('[!] Device is in recovery, please reboot into Android. Abort.')
		sys.exit(1)

	print('[*] Device found')

# command execution
def exe(command, *arguments, check_return=True):
	run_args = [ADB_PATH, command, *arguments]
	process = subprocess.run(run_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	if b'error: no devices/emulators found' in process.stderr:
		print('[!] No device found, please connect your phone. Abort.')
		sys.exit(1)

	if check_return and process.returncode != 0:
		print('[!] ADB command failed. Abort.')
		print(f'[!] Command: {" ".join(run_args)}')
		sys.exit(1)

	return process.stdout.decode('utf8')

def kill():
	return exe('kill-server')

def start():
	return exe('start-server')

def shell(*commands):
	return exe('shell', ' && '.join(commands))

def reboot():
	print('[*] Rebooting device. DO NOT UNPLUG!')
	return exe('reboot')

def wait():
	return exe('wait-for-device')

def push(a, b):
	return exe('push', a, b)

def uninstall(pkg, keep_data=False):
	k = ''
	if keep_data:
		k = ' -k'

	return exe('shell', 'cmd package uninstall {} {}'.format(k, pkg), check_return=False)

def install(pkg):
	return exe('install', pkg)

def mkdir(dir):
	return shell('mkdir ' + dir)

def rmdir(dir):
	return shell('rm -rf ' + dir)

def setting(scope, key, value):
	return shell('settings put {} {} "{}"'.format(scope, key, value))

def set_global(**pairs):
	for key, val in pairs.items():
		setting('global', key, str(val))

def set_secure(**pairs):
	for key, val in pairs.items():
		setting('secure', key, str(val))

def set_system(**pairs):
	for key, val in pairs.items():
		setting('system', key, str(val))

def enable_overlays(*overlays):
	for overlay in overlays:
		shell('cmd overlay enable ' + overlay)
