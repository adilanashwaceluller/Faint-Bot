import discord
from discord.ext import commands
import asyncio
import datetime
import time
import psutil

class BotInfoCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    self.client.launch_time = datetime.datetime.now()



  @commands.command(aliases=["p"])
  @commands.guild_only()
  async def ping(self, ctx):
    uptime1 = datetime.datetime.now() - self.client.launch_time
    uptime2 = str(uptime1)
    uptime3 = uptime2[0:10]
    embed=discord.Embed(description=f"```Ping      ;;   {round(self.client.latency * 1000)}ms \nUptime    ;;   {uptime3} ```", color=0x2f3136)
    embed.set_author(name="Faint Ping", icon_url="https://cdn.discordapp.com/avatars/870984698007007242/e1a5463f4e52a6ff2d7c3be4c8c70b07.webp?size=1024")
    embed.set_footer(text = f"Faint  |  Developed by Geb")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.guild_only()
  async def invite(self, ctx):
    embed = discord.Embed(description=f"[Bot Invite](https://discord.com/api/oauth2/authorize?client_id=870984698007007242&permissions=8&scope=bot%20applications.commands)\n[Support Server](https://discord.gg/5BvzxXkMjb)", color=0x2f3136)
    embed.set_footer(text = f"Faint  |  Developed by Geb")
    await ctx.send(embed=embed)
    
  @commands.command(aliases=["c"])
  @commands.guild_only()
  async def credits(self, ctx):
    embed = discord.Embed(description=f"Developer - Geb#0420\nClick [**here**](https://discord.com/users/456857241593708554) to see their profile!", color=0x2f3136)
    await ctx.send(embed=embed)

  @commands.command(aliases=['info', 'bot'])
  @commands.guild_only()
  async def botinfo(self, ctx):
    ram=str(psutil.virtual_memory()[2])+'%'
    cpu=str(psutil.cpu_percent())+'%'
    uptime1 = datetime.datetime.now() - self.client.launch_time
    uptime2 = str(uptime1)
    uptime3 = uptime2[0:10]
    embed=discord.Embed(color=0x2f3136)
    embed.set_author(name="Faint Info", icon_url="https://cdn.discordapp.com/avatars/870984698007007242/e1a5463f4e52a6ff2d7c3be4c8c70b07.webp?size=1024")
    embed.add_field(name="Bot", value=f"```Servers       ;;       {len(self.client.guilds)} \nUsers         ;;       {len(self.client.users)} \nVersion       ;;       v1.0 \nShards        ;;       1 ```", inline=False)
    embed.add_field(name="Hosting", value=f"```Python        ;;       v3.8.10 \nUptime        ;;       {uptime3} \nCPU Usage     ;;       {cpu} \nRAM Usage     ;;       {ram}```", inline=False)
    embed.add_field(name="Latency", value=f"```Shards        ;;       {round(self.client.latency * 1000)}ms (avr)\n  Shard 1     ;;       {round(self.client.latency * 1000)}ms```", inline=False)
    embed.set_footer(text = f"Faint  |  Developed by Geb")
    await ctx.send(embed=embed)


def setup(client):
  client.add_cog(BotInfoCog(client))