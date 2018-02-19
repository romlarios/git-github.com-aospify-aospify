#!/system/bin/sh

echo 'Disabling packages...'

for pkg in $(cat debloat_pkg.txt); do
	pm disable-user $pkg >/dev/null 2>&1
done

echo 'All packages disabled!'
