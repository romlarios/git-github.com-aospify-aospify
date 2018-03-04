#!/system/bin/sh

cd "$(dirname "$0")"
echo 'Enabling packages...'

for pkg in $(cat debloat_pkg.txt); do
	pm enable $pkg >/dev/null 2>&1
done

echo 'All packages enabled!'
