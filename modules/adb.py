import os, sys

ADB_PATH = os.path.abspath('bin/' + sys.platform + '/adb')
if sys.platform == 'win32':
    ADB_PATH += '.exe'

# handle bin missing; call from main.py
def adb_check():
	if not os.path.isfile(ADB_PATH):
		print('[!] ADB binary not found. Abort.')
		sys.exit(1)
	print('[*] ADB check passed')

# shell execution
def exe(command):
	os.system(ADB_PATH + ' ' + command)

def kill():
	exe('kill-server')
	
def start():
	exe('start-server')
	
# adb shell
def shell(command):
	# TODO: silence output of shell
	exe('shell ' + command)
	
def push(a, b):
	exe('push {} {}'.format(a, b))
	
def install(pkg):
	exe('install ' + pkg) 
	
def mkdir(dir):
	shell('mkdir ' + dir)
	
def rmdir(dir):
	shell('rm -rf ' + dir)
