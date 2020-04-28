
from pypresence import Presence
import time
import gd
import asyncio
import os
from termcolor import cprint 
from pyfiglet import figlet_format
VERSION = "1.1.3"
cprint(figlet_format('PyGDRPC', font='small'))
print(f"PyGDRPC v{VERSION} \nStarting...")

def Wait (time, silent=False):
    string = "timeout " + str(time)
    if silent:
        string = string + " >nul"
    
    os.system(string)

try:
    memory = gd.memory.get_memory()
except RuntimeError:
    print("Run GD first!")
    Wait(10, True)
    exit()

smallimage = "none" # fallback in case of the difficulty face not being returned
client = gd.Client() 
client_id = '703049428822655048'
RPC = Presence(client_id)
print("Connecting...")
try:
    RPC.connect()
except:
    print("Failed to connect to Discord!")
    Wait(10, True)
else:
    print("Connected successfully!")

async def get_difficulty(level: gd.Level) -> str:
    try:
        level = await client.get_level(id)
    except gd.MissingAccess:
        editorlevel = True
    else:
        editorlevel = False
        base = level.difficulty.name.lower().split("_")
        if level.is_epic():
            base.append("epic")
        elif level.is_featured():
            base.append("featured")
        return '-'.join(base)
async def get_offical_difficulty(level: gd.Level) -> str:
    try:
        olevel = gd.Level.official(id)
    except gd.MissingAccess:
        editorlevel = True
    else:
        editorlevel = False
        base = olevel.difficulty.name.lower().split("_")
        return '-'.join(base).replace("easy", "hard")
print("\nRunning!")
while True:
    memory.reload()
    scenev = memory.get_scene_value()
    scene = memory.get_scene()
    ltypev = memory.get_level_type_value()
    ltype = memory.get_level_type()
    iseditor = memory.is_in_editor()
    name = memory.get_level_name()
    percent = str(memory.get_normal_percent())
    if scenev == 3 and iseditor == False and ltypev == 3:
        id = memory.get_level_id()
        smallimage = asyncio.run(get_difficulty(id))
        RPC.update(pid=memory.process_id, state=str(f"{name} ({percent}%)"), details="Playing a level", large_image="gd", small_image=asyncio.run(get_difficulty(id)))
    if scenev == 3 and iseditor:
        RPC.update(pid=memory.process_id, details="In the editor.", large_image="gd", small_image="cp")
    if scenev == 3 and iseditor == False and ltypev == 2:
        RPC.update(pid=memory.process_id, state=str(f"{name} ({percent}%)"), details="Playing an editor level", large_image="gd", small_image="cp")
    else:
        if ltypev == 0:
            RPC.update(pid=memory.process_id, state="     ", details="In menu", large_image="gd")
        else:
            if scenev == 9 and ltypev == 1:
                id = memory.get_level_id()
                olevel = gd.Level.official(id)
                name = olevel.name
                smallimage = asyncio.run(get_offical_difficulty(id))
                RPC.update(pid=memory.process_id, state=f"{name} ({percent}%)", details="Playing an official level", large_image="gd", small_image=smallimage)
    time.sleep(5)