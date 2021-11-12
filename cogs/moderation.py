import discord
from discord.ext import commands
import asyncio

class BotInfoCog(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  @commands.cooldown(rate=1, per=5, type=commands.BucketType.member)
  @commands.has_permissions(ban_members=True)
  @commands.guild_only()
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    if ctx.guild.id == "760869077756674088":
      await ctx.send("This command has been disabled in this server!")
      return
    else:
      if reason is None:
        reason1 = "No reason specified"
      else:
        reason1 = reason
      try:
        await member.ban(reason=f"{ctx.author} - {reason1}")
        await ctx.send(f'`{member}` was banned by `{ctx.author}` for **`{reason1}`**')
      except:
        await ctx.send(f'Something went wrong')

  @commands.command()
  @commands.guild_only()
  @commands.cooldown(rate=1, per=5, type=commands.BucketType.member)
  @commands.has_permissions(manage_channels=True)		  
  async def nuke(self, ctx, channel: discord.TextChannel = None):
        embed = discord.Embed(description=f"<@!{ctx.author.id}> **nuked** `{ctx.channel.name}`", descriptioninline=False, color=0x2f3136)
        embed.set_image(url="https://cdn.discordapp.com/attachments/854048083511607356/858751017776709632/tenor.gif")
        channel = channel or ctx.channel
        position = channel.position
        newchannel = await channel.clone(reason=f"Channel Nuked by {ctx.author}")
        await channel.delete()
        await newchannel.edit(position=position)
        await newchannel.send(embed=embed)

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  @commands.cooldown(rate=1, per=5, type=commands.BucketType.member)
  async def unban(self, ctx, *, member):
    if ctx.guild.id == "760869077756674088":
      await ctx.send("This command has been disabled in this server!")
      return
    else:
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split("#")

      for ban_entry in banned_users:
        user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user}')
        await user.send(f"You have been unbanned from {ctx.guild.name}.")
      return

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(kick_members=True)
  @commands.cooldown(rate=1, per=5, type=commands.BucketType.member)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    if ctx.guild.id == "760869077756674088":
      await ctx.send("This command has been disabled in this server!")
      return
    else:
      if member is None:
        await ctx.send("Please mention a member!")
      else:
        reason1 = reason
      try:
        await member.kick(reason=f"{ctx.author} - {reason1}")
        await ctx.send(f'`{member}` was kicked by `{ctx.author}` for **`{reason1}`**')
      except:
        await ctx.send(f'Something went wrong')
          
  @commands.command()
  @commands.guild_only()
  @commands.cooldown(rate=1, per=5, type=commands.BucketType.member)
  @commands.has_permissions(manage_messages=True)
  async def slowmode(self, ctx, *, seconds:int=None):
    if seconds == None:
      await ctx.channel.edit(slowmode_delay = 0)
      await ctx.send(f"Removed the slowmode for this channel!")
      return
    if seconds == 0:
      await ctx.channel.edit(slowmode_delay = 0)
      await ctx.send(f"Removed the slowmode for this channel!")
      return
    else:
      await ctx.channel.edit(slowmode_delay=seconds)
      await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")
  
def setup(client):
  client.add_cog(BotInfoCog(client))