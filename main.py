import sys, os

# add the modules to the python path to allow imports
sys.path.insert(0, 'modules')

# import each required module using its filename
import adb
import debloat
import install
import setup

def splash():
	# TODO: replace with cool ASCII art
	print('''AOSPify tytydraco; kdrag0n''')

def main():
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	print(os.getcwd())
	splash()
	adb.adb_check()
	debloat.debloat()
	install.install()
	setup.setup()

main()
