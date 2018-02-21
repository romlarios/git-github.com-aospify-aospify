import os, sys

sys.path.insert(0, 'modules')
import adb

# paths are in reference to main.py so they will be localized at ./AOSPify/
_AOSPIFY_LOCAL = '/sdcard/aospify/'
_SCRIPT_DEBLOAT = './device/debloat.sh'
_SCRIPT_REBLOAT = './device/rebloat.sh'
_SCRIPT_DEBLOAT_PKG = './device/debloat_pkg.txt'

def debloat():
	# remove local dir and recreate for smoother updates
	adb.rmdir(_AOSPIFY_LOCAL)
	adb.mkdir(_AOSPIFY_LOCAL)
	
	# push script and list
	adb.push(os.path.abspath(_SCRIPT_DEBLOAT), _AOSPIFY_LOCAL)
	adb.push(os.path.abspath(_SCRIPT_DEBLOAT_PKG), _AOSPIFY_LOCAL)
	
	# give it +x perms
	adb.shell('chmod +x ' + _AOSPIFY_LOCAL + 'debloat.sh')
	
	# run debloat script
	adb.shell('cd /sdcard/aospify/; sh ' + _AOSPIFY_LOCAL + 'debloat.sh')
	
	# clean up
	adb.rmdir(_AOSPIFY_LOCAL)
	
def rebloat():
	# remove local dir and recreate for smoother updates
	adb.rmdir(_AOSPIFY_LOCAL)
	adb.mkdir(_AOSPIFY_LOCAL)
	
	# push script and list
	adb.push(os.path.abspath(_SCRIPT_DEBLOAT), _AOSPIFY_LOCAL)
	adb.push(os.path.abspath(_SCRIPT_DEBLOAT_PKG), _AOSPIFY_LOCAL)
	
	# TODO: fix literal insertion of final var @kdrag0n	
	# give it +x perms
	adb.shell('chmod +x ' + _AOSPIFY_LOCAL + 'rebloat.sh')
	
	# run debloat script
	adb.shell('cd /sdcard/aospify/; sh ' + _AOSPIFY_LOCAL + 'rebloat.sh')
	
	# clean up
	adb.rmdir(_AOSPIFY_LOCAL)
	