![Python App](https://github.com/SpookyBear0/pygdrpc/workflows/Python%20App/badge.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bc38c4e9065646a4976c8a021456d63c)](https://www.codacy.com/manual/SpookyBear0/pygdrpc?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SpookyBear0/pygdrpc&amp;utm_campaign=Badge_Grade)

# PyGDRPC 1.1.3
Geometry Dash rich presence, rewritten in Python!
  
![Example](https://i.imgur.com/hoMXIHh.png)
## Features:
- Level name and normal mode percentage
- Shows when you are in the editor (No name for security)
- Difficulty faces
- Name and normal mode percentage on local levels
- Shows when you are in menu
 
## How to use:
1. Download exe from releases
2. Open Geometry Dash (Note: GDPS don't work)
3. Start `pygdrpc.exe`

## Compiling
If you want to get the latest devoloper version right off the master branch, you can build it yourself.

**Requirements**

- Python >=3.6
- All modules in `requirements.txt` (`pip install -r requirements.txt`)
- Pyinstaller module (`pip install pyinstaller`)

### Building
 
1. Clone repo
2. CD to the folder you want to compile from in command prompt.
3. Run the command `python3 -m PyInstaller -F --hiddenimport pkg_resources.py2_warn -i assets/gd.ico pygdrpc.py` (if it says command not found - try replacing `python3` with `python` or `py`)
4. Wait for it to finish then go in the newly created folder "dist", and your .exe should be waiting there.
 
## Planned Features:
- None at the moment, if you want a feature, make an issue.
 
## Credits:
- Nekit: Showing me how to use the memory part of gd.py and more


**Please tell me if you like this program. Make an issue if you want to suggest features.**
