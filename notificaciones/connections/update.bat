@echo off
setlocal enableDelayedExpansion
set soeid=abcd

	set "val1=>"
	set "val2=_"
	set "str=%val1%%soeid%%val2%"

	echo !str!
set ip_address_string="IP Address"
rem Uncomment the following line when using Windows 7 (with removing "rem")!
set ip_address_string="IPv4 Address"
echo Network Connection Test
set h= "host":
for /f "usebackq tokens=2 delims=:" %%f in (`ipconfig ^| findstr /c:%ip_address_string%`) do (	
	echo%%f 
)
	set ip < ip.txt
	
	echo%ip% 
	rem echo/|set /p = "" ,
pause