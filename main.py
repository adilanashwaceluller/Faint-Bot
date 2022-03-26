import discord
import asyncio
from discord import Intents
from discord.ext import commands
import json
from discord.utils import get
import time
import sys
import os
import os.path

try:
    with open("config.json") as f:
        geb1 = json.load(f)
except:
    while 1 == 1:
        print(f"Failed xd - check config.json file")

with open("config.json") as f:
    token1 = geb1["token"]
    prefix1 = geb1["prefix"]

intents = discord.Intents.all()
intents = Intents.default()
intents.members = True
geb = commands.Bot(
  command_prefix = prefix1,
  allowed_mentions=discord.AllowedMentions(users=True, everyone=False, roles=False, replied_user=False),
  help_command=None,
  intents = intents,
)

async def status_task():
    while True:
        
        await geb.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(geb.users)} Users!"))
        await asyncio.sleep(10)
        await geb.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(geb.guilds)} Servers!"))
        await asyncio.sleep(10)

@geb.event
async def on_ready():
    print('Logged in as {0.user}'.format(geb))
    geb.loop.create_task(status_task())

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    geb.load_extension(f'cogs.{filename[:-3]}')
    
geb.run(token1)
