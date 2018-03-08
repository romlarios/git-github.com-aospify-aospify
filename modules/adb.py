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
def exe(command, *arguments):
	process = subprocess.run([ADB_PATH, command, *arguments], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	if b'error: no devices/emulators found' in process.stderr:
		print('[!] No device found, please connect your phone. Abort.')
		sys.exit(1)

	if process.returncode != 0:
		print('[!] ADB command failed. Abort.')
		sys.exit(1)

	return process.stdout.decode('utf8')

def kill():
	return exe('kill-server')

def start():
	return exe('start-server')

def shell(command):
	return exe('shell', command)

def reboot():
	return exe('reboot')

def wait():
	return exe('wait-for-device')

def push(a, b):
	return exe('push', a, b)

def install(pkg):
	return exe('install', pkg)

def mkdir(dir):
	return shell('mkdir ' + dir)

def rmdir(dir):
	return shell('rm -rf ' + dir)
