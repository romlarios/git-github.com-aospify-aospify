import os, sys

sys.path.insert(0, 'modules')
import adb

# paths are relative to main.py so they will be localized at ./AOSPify/
AOSPIFY_LOCAL = '/sdcard/aospify/'
SCRIPT_DEBLOAT = './device/debloat.sh'
SCRIPT_REBLOAT = './device/rebloat.sh'
LIST_DEBLOAT_PKG = './device/debloat_pkg.txt'

def debloat():
	# remove local dir and recreate for smoother updates
	adb.rmdir(AOSPIFY_LOCAL)
	adb.mkdir(AOSPIFY_LOCAL)
	
	# push script and list
	adb.push(os.path.abspath(SCRIPT_DEBLOAT), AOSPIFY_LOCAL)
	adb.push(os.path.abspath(SCRIPT_DEBLOAT_PKG), AOSPIFY_LOCAL)
	
	# give it +x perms
	adb.shell('chmod +x ' + AOSPIFY_LOCAL + 'debloat.sh')
	
	# run debloat script
	adb.shell('cd /sdcard/aospify/; sh ' + AOSPIFY_LOCAL + 'debloat.sh')
	
	# clean up
	adb.rmdir(AOSPIFY_LOCAL)
	
def rebloat():
	# remove local dir and recreate for smoother updates
	adb.rmdir(AOSPIFY_LOCAL)
	adb.mkdir(AOSPIFY_LOCAL)
	
	# push script and list
	adb.push(os.path.abspath(SCRIPT_DEBLOAT), AOSPIFY_LOCAL)
	adb.push(os.path.abspath(LIST_DEBLOAT_PKG), AOSPIFY_LOCAL)
	
	# TODO: fix literal insertion of final var @kdrag0n	
	# give it +x perms
	adb.shell('chmod +x ' + AOSPIFY_LOCAL + 'rebloat.sh')
	
	# run debloat script
	adb.shell('cd ' + AOSPIFY_LOCAL + '; sh ' + AOSPIFY_LOCAL + 'rebloat.sh')
	
	# clean up
	adb.rmdir(AOSPIFY_LOCAL)
	