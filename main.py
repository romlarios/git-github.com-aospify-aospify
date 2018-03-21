#!/usr/bin/env python3

import os
import sys
import time
import inspect
import modules as mod

def splash():
	print('''
 █████╗  ██████╗ ███████╗██████╗ ██╗███████╗██╗   ██╗
██╔══██╗██╔═══██╗██╔════╝██╔══██╗██║██╔════╝╚██╗ ██╔╝
███████║██║   ██║███████╗██████╔╝██║█████╗   ╚████╔╝
██╔══██║██║   ██║╚════██║██╔═══╝ ██║██╔══╝    ╚██╔╝
██║  ██║╚██████╔╝███████║██║     ██║██║        ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝        ╚═╝
--------------------------------------
Samsung Root-less AOSP Experience
Made by: tytydraco, kdrag0n''')

packaged = False

def main():
	if not hasattr(sys.modules[__name__], '__file__'):
		__file__ = sys.executable
		packaged = True # TODO: print some README here

	os.chdir(os.path.dirname(os.path.realpath(__file__)))

	splash()
	mod.adb_check()
	mod.device_check()
	mod.model()
	mod.debloat()
	mod.install()
	mod.media()

	# apply settings AFTER reboot and detect plugged in
	mod.reboot()
	mod.wait()
	time.sleep(5)

	mod.settings()
	mod.reboot()

	print('[*] Done! Enjoy your better phone. You can unplug.')


if __name__ == '__main__':
	main()
