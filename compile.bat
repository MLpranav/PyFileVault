pyinstaller --onefile --windowed --icon=PyFileVault.ico PyFileVault.py --add-data "PyFileVault.ico;."
move dist\* .
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q __pycache__
del PyFileVault.spec