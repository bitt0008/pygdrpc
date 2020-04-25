from pypresence import Presence
import time
import gd
import asyncio
import os
version = "1.0.2b"
print(f"Version is {version}")
smallimage = "none"
client = gd.Client()
try:
    memory = gd.memory.get_memory()
except RuntimeError:
    print("Open Geometry Dash before running this!")
    os.system("PAUSE")
    exit()
client_id = '703049428822655048'
RPC = Presence(client_id)
print("Connecting.")
try:
    RPC.connect()
except:
    print("Failed to connect to discord, try reopening it?")
else:
    print("Connected successfully!")
async def get_level_from_id(id):
    try:
        level = await client.get_level(id)
        return level.name
    except gd.MissingAccess:
        if playinglevel != "Menu":
            return "Editor level"
async def if_playing_level(id):
    try:
        level = await client.get_level(id)
    except gd.MissingAccess:
        if id == 1400 or id == 1399 and percent != "   ":
            smallimage = "cp"
            return "Playing an editor level."
        else:
            return "Menu."
    else:
        return "Playing a level."
async def get_difficulty(level: gd.Level) -> str:
    if id != 1404 and id != 0 and id != 1400 and id != 1399 and id != 4294967295 and id != 1408:
        level = await client.get_level(id)
    if playinglevel == "Playing a level.":
        base = level.difficulty.name.lower().split('_')
        if level.is_epic():
            base.append('epic')
        elif level.is_featured():
            base.append('featured')
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
    id = memory.get_level_id()
    percent = memory.get_normal_percent()
    playinglevel = asyncio.run(if_playing_level(id))
    if percent == 0:
        percent = "   "
    else:
        percent = "(" + str(percent) + "%)"
    name = asyncio.run(get_level_from_id(id))
    if playinglevel == "Playing a level.":
        smallimage = asyncio.run(get_difficulty(id))
    if percent == "   ":
        playinglevel = "Menu"
    if id != 1404 and id != 0 and id != 1400 and id != 1399 and id != 4294967295 and id != 1408:
        playinglevel = "Playing a level."
    if smallimage == "none":
        RPC.update(state=str(f"{name} {percent}"), details=playinglevel, large_image="gd")
    else:
        RPC.update(state=str(f"{name} {percent}"), details=playinglevel, large_image="gd", small_image=smallimage)
    time.sleep(5)