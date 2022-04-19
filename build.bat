rmdir /s /q dist
pyinstaller FluentCalculator.py --onefile --windowed --collect-data sv_ttk --icon "Calculator.ico"
del FluentCalculator.spec
xcopy Calculator.ico dist