#!/system/bin/sh

echo 'Disabling packages...'

for pkg in $(cat uninstall_pkg.txt); do
	pm uninstall --user 0 -k $pkg >/dev/null 2>&1
done

echo 'All packages disabled!'
