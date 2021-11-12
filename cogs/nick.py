import discord
from discord.ext import commands
import random
import string


class NickCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_nicknames=True)
  @commands.guild_only()
  async def nick(self, ctx, member: discord.Member, *, nickname=None):
    if nickname is None:
      await ctx.send("Incorect usage!")
    else:
      await member.edit(nick=nickname)
      await ctx.send(f"Changed nickname for {member} to `{nickname}`!")

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_nicknames=True)
  async def modnick(self, ctx, member: discord.Member):
    if member is None:
      await ctx.send("Please mention someone!")
    else:
      await member.edit(nick=f"Moderated Nickname {(random.randint(10000, 99999))}")
      await ctx.send(f"`{member}`'s nickname was moderated!")

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_nicknames=True)
  async def resetnick(self, ctx, member: discord.Member):
      username = f"{member.name}"
      await member.edit(nick=username)
      await ctx.send(f"Reset nickname for {member}!")


def setup(client):
  client.add_cog(NickCog(client))