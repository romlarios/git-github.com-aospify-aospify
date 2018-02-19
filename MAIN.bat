:<<"::CMDLITERAL"
@ECHO OFF
GOTO :CMDSCRIPT
::CMDLITERAL

cd "$(dirname "$0")"
sh debloat.bat
sh install.bat
sh setup.bat

:CMDSCRIPT
debloat.bat
install.bat
setup.bat
