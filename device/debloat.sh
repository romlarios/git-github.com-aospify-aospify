#!/system/bin/sh

cd "$(dirname "$0")"
echo 'Uninstalling packages...'

for pkg in $(cat debloat_pkg.txt); do
	pm uninstall --user 0 $pkg >/dev/null 2>&1
done

echo 'All packages uninstalled!'
