# py_to_exe
Convert a .py (Python) file to .exe (executable)

> pip install pyinstaller  or (pip install -r .\requirement.txt)

# Make python file
## convert .py file to exe: 

> syntax : pyinstaller [filename]

> example : pyinstaller test1.py

> -> check .exe file in dist folder

# above steps create an environment with lot of files and folders, 
# hence to pack all in one single .exe file we use:

> syntax : pyinstaller --onefile [filename]

> example : pyinstaller --onefile test2.py

# if you do not wish to run a cmd in background when opening a .exe file then we use: 
# (Use test3.py for this step)

> syntax : pyinstaller --onefile --windowed [filename]

> example : pyinstaller --onefile --windowed test3.py

# if you wish to change icon of .exe file: 
# (you might have to change the view in windows to check the icon)

> syntax : pyinstaller --onefile --windowed --icon "[icon path]" [filename]

> example : pyinstaller --onefile --windowed --icon "icon\sample_icon.ico" test4.py

# if you wish to perform all the above tasks with the help of GUI:

> pip install auto-py-to-exe

> auto-py-to-exe

