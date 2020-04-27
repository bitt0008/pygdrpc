# pygdrpc 1.1.0
 Geometry Dash rich presence, rewritten in python!
 
 ![Example](https://i.imgur.com/hoMXIHh.png)
 ## Features:
 - Level name and normal mode percentage
 - Shows when you are in the editor (No name for security)
 - Difficulty faces
 - Name and normal mode percentage on local levels
 - Shows when you are on the menu
 ## How to use:
 1. Download exe from releases
 2. Open Geometry Dash (GDPS's don't work)
 3. Start the .exe file you downloaded
 4. Perfection

 ## Compiling
 If you want to get the lastest devoloper version right of the master branch, you can compile the code yourself. (make sure you have enough computer knowledge though)

**Requirements**

- Python 3.6-3.8

- All modules in requirements.txt (pip install -r requiremennts.txt)

- Pyinstaller module (pip install pyinstaller)

 ### Building the .exe
1. Clone repo
2. CD to the folder you want to compile from in command prompt.
3. Run the command "python3 -m PyInstaller -F --hiddenimport pkg_resources.py2_warn -i assets/gd.ico pygdrpc.py" (if it says command not found try replacing python3 with python or py.)
4. Wait for it to finish then go in the newly created folder "dist", and your .exe should be waiting there.
 ## Planned Features:
 - None at the moment, if you want a feature, make an issue.
 ## Credits:
**Nekit: Showing me how to use the memory part of gd.py and more**
