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

# command execution
def exe(command, *arguments):
	subprocess.check_output(ADB_PATH, command, *arguments)

def kill():
	return exe('kill-server')

def start():
	return exe('start-server')

def shell(command):
	return exe('shell', command)

def push(a, b):
	return exe('push', a, b)

def install(pkg):
	return exe('install', pkg)

def mkdir(dir):
	return shell('mkdir ' + dir)

def rmdir(dir):
	return shell('rm -rf ' + dir)
