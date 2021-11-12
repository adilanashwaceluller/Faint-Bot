import discord
from discord.ext import commands
import asyncio

class InfoCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.guild_only()
  async def membercount(self, ctx):
    member_count = len(ctx.guild.members)
    true_member_count = len([m for m in ctx.guild.members if not m.bot])
    total_bots = member_count - true_member_count
    embed = discord.Embed(title=f"{ctx.guild.name}", description=f"{member_count} total members!\n{true_member_count} total humans!\n{total_bots} total bots!", color=0x2f3136)
    await ctx.send(embed=embed)
    
  @commands.command()
  @commands.guild_only()
  async def serverowner(self, ctx):
    owner = ctx.guild.owner
    await ctx.send(f"{ctx.guild.name}'s owner is {owner}")

  @commands.command()
  @commands.guild_only()
  async def banner(self, ctx):
      embed2 = discord.Embed(title=f"{ctx.guild.name}'s banner", color=0x2f3136)
      embed2.set_image(url=f"{ctx.guild.banner_url}")
      await ctx.send(embed=embed2)

  @commands.command(aliases=['av'])
  @commands.guild_only()
  async def avatar(self, ctx, *,  avamember: discord.Member=None):
    if avamember is None:
      embed = discord.Embed(title=f"{ctx.author.name}'s avatar", color=0x2f3136)
      embed.set_image(url=f"{ctx.author.avatar_url}")
      await ctx.send(embed=embed)
    else:
      userAvatarUrl = avamember.avatar_url
      embed2 = discord.Embed(title=f"{avamember.name}'s avatar", color=0x2f3136)
      embed2.set_image(url=f"{userAvatarUrl}")
      await ctx.send(embed=embed2)
      
  @commands.command()
  @commands.guild_only()
  async def joined(self, ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f"{member.name} joined in {member.joined_at}")
      
def setup(client):
  client.add_cog(InfoCog(client))