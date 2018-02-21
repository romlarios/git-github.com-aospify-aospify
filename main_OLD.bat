:<<"::CMDLITERAL"
@ECHO OFF
GOTO :CMDSCRIPT
::CMDLITERAL

cd "$(dirname "$0")"
sh modules/debloat.bat
sh modules/install.bat
sh modules/setup.bat

:CMDSCRIPT
modules\debloat.bat
modules\install.bat
modules\setup.bat
