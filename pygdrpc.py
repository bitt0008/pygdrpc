from pypresence import Presence
import time
import gd
import asyncio
version = "1.0.3b"
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
async def get_level_from_id(id):
    global playinglevel
    try:
        level = await client.get_level(id)
        return level.name
    except gd.MissingAccess:
        if playinglevel != "Menu":
            return "Editor level"
async def if_playing_level():
    scenev = memory.get_scene_value()
    scene = memory.get_scene()
    if scenev == 3:
        playinglevel = "Playing a level."
        return "Playing a level."
    if scene == "Search" or "Online" or "Select" or "Leaderboard" or "Main" or "Main Levels":
        playinglevel = "Menu"
        return "Menu"
    if scene == "Main Level" or "The Challenge":
        playinglevel = "Playing a robtop level."
        return "Playing a robtop level."
async def get_difficulty(level: gd.Level) -> str:
    if id != 1404 and id != 0 and id != 1400 and id != 1399 and id != 4294967295 and id != 1408:
        level = await client.get_level(id)
        base = level.difficulty.name.lower().split('_')
        if level.is_epic():
            base.append("epic")
        elif level.is_featured():
            base.append("featured")
        if len(base) == 1:
            myorder = [0]
        if len(base) == 2:
            if "demon" in base:
                myorder = [1,0]
            else:
                myorder = [0,1]
        if len(base) == 3:
            myorder = [1,0,2]
        base = [base[i] for i in myorder]    
        return '-'.join(base)
while True:
    memory.reload()
    scenev = memory.get_scene_value()
    scene = memory.get_scene()
    id = memory.get_level_id()
    percent = memory.get_normal_percent()
    playinglevel = asyncio.run(if_playing_level())
    if percent == 0:
        percent = "   "
    else:
        percent = "(" + str(percent) + "%)"
    name = asyncio.run(get_level_from_id(id))
    if scenev == 0 or 1 or 2 or 4 or 6 or 7 or 8 and smallimage == "none":
        RPC.update(state="     ", details="Menu", large_image="gd")
    if scenev == 9 and smallimage == "none":
        RPC.update(state="     ", details="Playing a robtop level.", large_image="gd")
    else:
        smallimage = asyncio.run(get_difficulty(id))
        RPC.update(state=str(f"{name} {percent}"), details=playinglevel, large_image="gd", small_image=smallimage)
    if scenev == "Playing a level.":
        RPC.update(state=str(f"{name} {percent}"), details=playinglevel, large_image="gd", small_image=smallimage)
    time.sleep(5)