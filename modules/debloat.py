import os, sys

sys.path.insert(0, 'modules')
import adb

# paths are relative to main.py
DEVICE_DIR = '/sdcard/aospify/'
SCRIPT_DEBLOAT = 'device/debloat.sh'
SCRIPT_UNINSTALL = 'device/uninstall.sh'
SCRIPT_REBLOAT = 'device/rebloat.sh'
PKG_DEBLOAT_LIST = 'device/debloat_pkg.txt'
PKG_UNINSTALL_LIST = 'device/uninstall_pkg.txt'

def debloat():
	# remove local dir and recreate for smoother updates
	adb.rmdir(DEVICE_DIR)
	adb.mkdir(DEVICE_DIR)
	
	# push script and list
	adb.push(SCRIPT_DEBLOAT, DEVICE_DIR)
	adb.push(PKG_DEBLOAT_LIST, DEVICE_DIR)
	adb.push(SCRIPT_UNINSTALL, DEVICE_DIR)
	adb.push(PKG_UNINSTALL_LIST, DEVICE_DIR)
	
	# run script
	adb.shell('sh ' + DEVICE_DIR + 'debloat.sh')
	adb.shell('sh ' + DEVICE_DIR + 'uninstall.sh')
	
	# clean up
	adb.rmdir(DEVICE_DIR)
	
def rebloat():
	# remove local dir and recreate for smoother updates
	adb.rmdir(DEVICE_DIR)
	adb.mkdir(DEVICE_DIR)
	
	# push script and list
	adb.push(SCRIPT_REBLOAT, DEVICE_DIR)
	adb.push(PKG_DEBLOAT_LIST, DEVICE_DIR)
	
	# run script
	adb.shell('sh ' + DEVICE_DIR + 'rebloat.sh')
	
	# clean up
	adb.rmdir(DEVICE_DIR)	
