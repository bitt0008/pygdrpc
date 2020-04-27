from pypresence import Presence
import time
import gd
import asyncio
version = "1.1.0"
print(f"Version is {version}")
smallimage = "none"
client = gd.Client()
try:
    memory = gd.memory.get_memory()
except RuntimeError:
    print("Open Geometry Dash before running this!")
client_id = '703049428822655048'
RPC = Presence(client_id)
print("Connecting...")
try:
    RPC.connect()
except:
    print("Failed to connect to discord, try reopening it?")
else:
    print("Connected successfully!")

async def if_playing_level():
    scenev = memory.get_scene_value()
    scene = memory.get_scene()
    if scenev == 3:
        playinglevel = "Playing a level."
        return "Playing a level."
    if scene == "Main Level" or "The Challenge":
        playinglevel = "Playing an official level."
        return "Playing an official level."
    else:
        playinglevel = "Menu"
        return "Menu"

async def get_difficulty(level: gd.Level) -> str:
    if id != 1404 and id != 0 and id != 1400 and id != 1399 and id != 4294967295 and id != 1408:
        try:
            level = await client.get_level(id)
        except gd.MissingAccess:
            editorlevel = True
        else:
            editorlevel = False
            base = level.difficulty.name.lower().split('_')
            if level.is_epic():
                base.append("epic")
            elif level.is_featured():
                base.append("featured")
            return '-'.join(base)

while True:
    memory.reload()
    scenev = memory.get_scene_value()
    scene = memory.get_scene()
    ltypev = memory.get_level_type_value()
    ltype = memory.get_level_type()
    iseditor = memory.is_in_editor()
    id = memory.get_level_id()
    percent = memory.get_normal_percent()
    playinglevel = asyncio.run(if_playing_level())
    if percent == 0:
        percent = "   "
    else:
        percent = "(" + str(percent) + "%)"
    name = memory.get_level_name()
    if scenev == 3 and iseditor == False and ltypev == 3 and percent == "   ":
        smallimage = asyncio.run(get_difficulty(id))
        RPC.update(pid=memory.process_id, state=str(f"{name} {percent}"), details=playinglevel, large_image="gd", small_image=asyncio.run(get_difficulty(id)))
    if scenev == 3 and iseditor and ltypev != 2:
        RPC.update(pid=memory.process_id, details="In the editor.", large_image="gd")
    if scenev == 3 and iseditor == False and ltypev == 2:
        RPC.update(pid=memory.process_id, state=str(f"{name} {percent}"), details="Playing an editor level.", large_image="gd")
    else:
        if scenev == scenev != 3 and iseditor == False and ltypev != 2 and ltypev != 3 and ltypev != 1 or percent == "   " or None:
            RPC.update(pid=memory.process_id, state="     ", details="Menu", large_image="gd")
        else:
            if scenev == 9 and ltypev == 1:
                smallimage = asyncio.run(get_difficulty(id))
                RPC.update(pid=memory.process_id, state="     ", details="Playing an official level.", large_image="gd", small_image=smallimage)
    time.sleep(5)
