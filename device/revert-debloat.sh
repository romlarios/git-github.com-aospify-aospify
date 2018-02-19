#!/system/bin/sh

echo 'Re-enabling packages...'

for pkg in $(cat debloat_pkg.txt); do
	pm enable $pkg >/dev/null 2>&1
done

echo 'All packages re-enabled!'
