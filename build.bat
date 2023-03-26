cd src
rmdir /s /q dist
pyinstaller main.py --onedir --windowed --collect-data sv_ttk --icon "icon.ico" --add-data "config.json;."
del main.spec
xcopy icon.ico dist
cd dist
ren main.exe FluxCalc.exe