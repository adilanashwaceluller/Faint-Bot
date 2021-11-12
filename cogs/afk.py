import discord
from discord.ext import commands
import asyncio
import random


class afkCog(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  @commands.guild_only()
  async def afk(self, ctx, *, reason: str=None): 
        if reason == None:
            reason = 'No Reason Specifed'
        current_nick = ctx.author.nick
        embed = discord.Embed(color=0x2f3136)
        embed.description=f"{ctx.author.mention} Is Now Afk | {reason}"
        await ctx.send(embed=embed)
        try:
          await ctx.author.edit(nick=f"[AFK] {ctx.author.name}") 
        except:
          return
        
        msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        embed = discord.Embed(color=0x2f3136)
        try:
          await ctx.author.edit(nick=current_nick)
        except: 
          embed.description=f"{ctx.author.mention} you are no longer afk!"
          await ctx.send(embed=embed)
    
def setup(client):
  client.add_cog(afkCog(client))