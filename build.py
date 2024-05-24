import os
import PyInstaller.__main__ as py_installer
import shutil
from distutils.dir_util import copy_tree

version = "Unofficial v146 Build"

print("\nBuilding Dashboard...")
py_installer.run([
    'manager.py',
'-i=assets/icon.ico',
    '-w',
    '-y',
    '-n=GWSL',
    #'--hidden-import=pkg_resources.py2_warn'
])

print("\nBuilding Service...")
py_installer.run([
    'main.py',
    '-i=assets/icon.ico',
    '-w',
    '-y',
    '-n=GWSL_service',
    '--hidden-import=pkg_resources',
    '--hidden-import=infi.systray',
    #'--hidden-import=pkg_resources.py2_warn'
])

print(f"\nCreating dist/GWSL_{version}")
try:
    os.mkdir(f"dist/GWSL_{version}")
except:
    print("Deleting Old Build")
    shutil.rmtree(f"dist/GWSL_{version}")
    os.mkdir(f"dist/GWSL_{version}")

print("Copying Assets...")
folders = ["assets", "locale", "PULSE", "PUTTY", "VCXSRV", "sv_ttk"]
for folder in folders:
    print("Merging:", folder)
    shutil.copytree(folder, f"dist/GWSL_{version}/" + str(folder))

print("Merging: Dashboard...")
copy_tree("dist/GWSL/", f"dist/GWSL_{version}/")

print("Merging: Service...")
copy_tree("dist/GWSL_service/", f"dist/GWSL_{version}/")

shutil.make_archive('GWSL_service', 'zip', 'dist')

