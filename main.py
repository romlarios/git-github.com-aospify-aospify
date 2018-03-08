#!/usr/bin/env python3

import os
import sys
import modules as mod

def splash():
	print('''
	_    ___  ____  ____  _  __
   / \\  / _ \\/ ___||  _ \\(_)/ _|_   _
  / _ \\| | | \\___ \\| |_) | | |_| | | |
 / ___ \\ |_| |___) |  __/| |  _| |_| |
/_/   \\_\\___/|____/|_|   |_|_|  \\__, |
								|___/
--------------------------------------
Samsung Root-less AOSP Experience
Made by: tytydraco, kdrag0n''')

def main():
	if getattr(sys, 'frozen', False):
		# frozen
		os.chdir(os.path.dirname(os.path.realpath(sys.executable)))
		# TODO: print a lot of README in steps
	else:
		# unfrozen
		os.chdir(os.path.dirname(os.path.realpath(__file__)))

	splash()
	mod.adb_check()
	mod.device_check()
	mod.debloat()
	mod.install()
	
	adb.reboot()
	
	# TODO: apply settings AFTER reboot
	
	mod.settings()


if __name__ == '__main__':
	main()
