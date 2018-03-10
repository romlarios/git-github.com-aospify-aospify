from tqdm import tqdm
from . import adb

# paths are relative to main.py
PKG_DEBLOAT_LIST = 'assets/debloat_pkgs.txt'

def debloat():
	print('[*] Debloating')

	# read debloat list
	with open('assets/debloat_pkgs.txt', 'rb') as f:
		debloat = f.read().decode('utf8').split('\n')
	if debloat[-1] == '':
		del debloat[len(debloat) - 1]  # final new line

	# fetch enabled package list
	enabled = adb.shell('pm list packages -e')

	# filter lists
	enabled = enabled.replace('package:', '')
	enabled = enabled.split('\n')
	debloat = set(debloat).intersection(enabled)

	if len(debloat) == 0:
		return

	# uninstall packages
	for pkg in tqdm(debloat, desc='Debloating'):
		adb.shell('pm uninstall --user 0 ' + pkg)
