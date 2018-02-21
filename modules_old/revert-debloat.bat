adb shell mkdir /sdcard/aospify
adb push ../device/revert-debloat.sh /sdcard/aospify/
adb push ../device/debloat_pkg.txt /sdcard/aospify/
adb shell sh /sdcard/aospify/debloat.sh
