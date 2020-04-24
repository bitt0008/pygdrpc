from pypresence import Presence
import time
import gd
import asyncio
smallicon = "none"
client = gd.Client()
try:
    memory = gd.memory.get_memory()
except RuntimeError:
    print("Open Geometry Dash before running this!")
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
        return ""
async def if_playing_level(id):
    try:
        level = await client.get_level(id)
        level
    except gd.MissingAccess:
        if percent == "   ":
            return "Menu"
        else:
            smallicon = "cp"
            return "Playing an editor level"
    else:
        return "Playing a level."
async def get_difficulty(level: gd.Level) -> str:
    level = await client.get_level(id)
    if playinglevel == "Playing a level.":
        base = level.difficulty.name.lower().split('_')
        if level.is_epic():
            base.append('epic')
        elif level.is_featured():
            base.append('featured')
        elif level.is_rated():
            base.append('rated')
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
    RPC.update(pid=memory.process_id, state=str(f"{name} {percent}"), details=playinglevel, large_image="gd", small_image=asyncio.run(get_difficulty(id)))
    time.sleep(10)