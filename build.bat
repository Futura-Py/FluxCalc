cd src
rmdir /s /q dist
pyinstaller main.py --onefile --windowed --collect-data sv_ttk --icon "icon.ico"
del main.spec
xcopy icon.ico dist
cd dist
ren main.exe FluxCalc.exe