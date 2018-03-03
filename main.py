import sys, os

# add the modules to the python path to allow imports
sys.path.insert(0, 'modules')

# import each required module using its filename
import adb
import debloat
import install
import setup

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
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	
	splash()
	adb.adb_check()
	debloat.debloat()
	install.install()
	setup.setup()

main()
