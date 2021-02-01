@echo off
echo cd "%cd%" > "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\cmm.bat"
echo "%cd%\runModules.bat" >> "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\cmm.bat"
echo pause >> "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\cmm.bat"