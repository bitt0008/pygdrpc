from pypresence import Presence
import time
import os
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
async def level_difficulty():
    level = await client.get_level(id)
    if playinglevel == "Playing a level.":
        if level.is_featured() == True:
            if str(level.difficulty) == "Auto":
                smallicon = "auto-featured"
            if str(level.difficulty) == "Easy":
                smallicon = "easy-featured"
            if str(level.difficulty) == "Normal":
                smallicon = "normal-featured"
            if str(level.difficulty) == "Hard":
                smallicon = "hard-featured"
            if str(level.difficulty) == "Harder":
                smallicon = "harder-featured"
            if str(level.difficulty) == "Insane":
                smallicon = "insane-featured"
            if str(level.difficulty) == "Easy Demon":
                smallicon = "demon-easy-featured"
            if str(level.difficulty) == "Medium Demon":
                smallicon = "demon-medium-featured"
            if str(level.difficulty) == "Hard Demon":
                smallicon = "demon-hard-featured"
            if str(level.difficulty) == "Insane Demon":
                smallicon = "demon-insane-featured"
            if str(level.difficulty) == "Extreme Demon":
                smallicon = "demon-extreme-featured"
        if level.is_epic() == True:
            if str(level.difficulty) == "Auto":
                smallicon = "auto-epic"
            if str(level.difficulty) == "Easy":
                smallicon = "easy-epic"
            if str(level.difficulty) == "Normal":
                smallicon = "normal-epic"
            if str(level.difficulty) == "Hard":
                smallicon = "hard-epic"
            if str(level.difficulty) == "Harder":
                smallicon = "harder-epic"
            if str(level.difficulty) == "Insane":
                smallicon = "insane-epic"
            if str(level.difficulty) == "Easy Demon":
                smallicon = "demon-easy-epic"
            if str(level.difficulty) == "Medium Demon":
                smallicon = "demon-medium-epic"
            if str(level.difficulty) == "Hard Demon":
                smallicon = "demon-hard-epic"
            if str(level.difficulty) == "Insane Demon":
                smallicon = "demon-insane-epic"
            if str(level.difficulty) == "Extreme Demon":
                smallicon = "demon-extreme-epic"
        if level.is_epic() == False and level.is_featured() == False:
            if str(level.difficulty) == "Auto":
                smallicon = "auto"
            if str(level.difficulty) == "Easy":
                smallicon = "easy"
            if str(level.difficulty) == "Normal":
                smallicon = "normal"
            if str(level.difficulty) == "Hard":
                smallicon = "hard"
            if str(level.difficulty) == "Harder":
                smallicon = "harder"
            if str(level.difficulty) == "Insane":
                smallicon = "insane"
            if str(level.difficulty) == "Easy Demon":
                smallicon = "demon-easy"
            if str(level.difficulty) == "Medium Demon":
                smallicon = "demon-medium"
            if str(level.difficulty) == "Hard Demon":
                smallicon = "demon-hard"
            if str(level.difficulty) == "Insane Demon":
                smallicon = "demon-insane"
            if str(level.difficulty) == "Extreme Demon":
                smallicon = "demon-extreme"
        if str(level.difficulty) == "NA":
                smallicon = "unrated"
        return smallicon
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
    RPC.update(pid=memory.process_id, state=str(f"{name} {percent}"), details=playinglevel, large_image="gd", small_image=asyncio.run(level_difficulty()))
    time.sleep(10)