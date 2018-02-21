import os

# TODO: support unix
_ADB_PATH = 'bin/adb.exe'

# private standalone bin check
def _adb_bin_exists():
	return (os.path.isfile(_ADB_PATH))
	
# handle bin missing; call from main.py
def adb_check():
	if not _adb_bin_exists:
		print('[!] ADB binary not found. Abort.')
		exit(1)
	print('[*] ADB check passed')

# shell execution
def exe(command):
	# TODO: support unix and implement bin utilization
	# os.system('./%s %s' % (_ADB_PATH, command))
	
	abs_path = os.path.abspath(_ADB_PATH)
	os.system('%s %s' % (abs_path, command))
	
	# os.system('adb %s' % command)

def kill():
	exe('kill-server')
	
def start():
	exe('start-server')
	
# adb shell
def shell(command):
	# TODO: silence output of shell
	exe('shell %s' % command)
	
def push(a, b):
	exe('push %s %s' % (a, b))
	
def install(pkg):
	exe('install %s' % pkg) 
	
def mkdir(dir):
	shell('mkdir %s' % dir)
	
def rmdir(dir):
	shell('rm -rf %s' % dir)
	