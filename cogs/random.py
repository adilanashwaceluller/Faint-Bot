import discord
from discord.ext import commands
import asyncio
import random


class randomCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.guild_only()
  async def wizz(self, ctx):
    if ctx.guild.id == "760869077756674088":
      await ctx.send("This command has been disabled in this server!")
      return
    else:
      message = await ctx.send(f"**Wizzing {ctx.guild.name}**")
      await asyncio.sleep(2.5)
      await message.edit(content=f"**Wizzing {ctx.guild.name}**\nBanning {len(ctx.guild.members)} members")
      await asyncio.sleep(4)
      await message.edit(content=f"**Wizzing {ctx.guild.name}**\nBanned {len(ctx.guild.members)} members <:success:878654513152663633>\nDeleting {len(ctx.guild.channels)} channels")
      await asyncio.sleep(4)
      await message.edit(content=f"**Wizzing {ctx.guild.name}**\nBanned {len(ctx.guild.members)} members <:success:878654513152663633>\nDeleted {len(ctx.guild.channels)} channels <:success:878654513152663633>")
      await asyncio.sleep(4)
      await message.edit(content=f"**Wizzing {ctx.guild.name}**\nBanned {len(ctx.guild.members)} members <:success:878654513152663633>\nDeleted {len(ctx.guild.channels)} channels <:success:878654513152663633>", delete_after=5.5)
      await asyncio.sleep(6)
      await ctx.send(f"`Wizzed {ctx.guild.name}`")
  
  @commands.command()
  @commands.guild_only()
  async def randomnumber(self, ctx):
    await ctx.send(f"{(random.randint(1, 999999999999999999))}")
  
  @commands.command(aliases=["8ball"])
  @commands.guild_only()
  async def _8ball(self, ctx, *, question=None):
    responses = ['As I see it, yes.',
             'Yes.',
             'Positive',
             'From my point of view, yes',
             'Convinced.',
             'Most Likley.',
             'Chances High',
             'No.',
             'Negative.',
             'Not Convinced.',
             'Perhaps.',
             'Not Sure',
             'Mayby',
             'I cannot predict now.']
    response = random.choice(responses)
    embed = discord.Embed(description=f"Question - {question}\nAnswer - {response}", color=0x2f3136)
    embed.set_footer(text = f"Faint  |  Developed by Geb")
    await ctx.send(embed=embed)
  
  @commands.command()
  @commands.guild_only()
  async def coinflip(self, ctx):
    choices = ['heads', 'tails']
    await ctx.send(f"{ctx.author.mention} I choose **{random.choice(choices)}**")
    
  @commands.command(aliases=['penis', 'ppsize', 'penissize'])
  @commands.guild_only()
  async def pp(self, ctx):
    if ctx.guild.id == "760869077756674088":
      await ctx.send("This command has been disabled in this server!")
      return
    else:
      if ctx.author.id == 660563979684544513:
        embed2= discord.Embed(description=f"{ctx.author.mention}'s pp size\n8===========================================================================D", color=0x2f3136)
        await ctx.send(embed=embed2)
        return
      else:
        pp = ['8====D', '8==============D', '8==D', '8======================D', '8======D', '8========D']
        embed= discord.Embed(description=f"{ctx.author.mention}'s pp size\n{random.choice(pp)}", color=0x2f3136)
      await ctx.send(embed=embed)
      
  @commands.command()
  @commands.guild_only()
  async def reportbug(self, ctx, *, bug):
    if ctx.author.id == None:
      return
    else:
      owner = self.client.get_user(660563979684544513)
      await owner.send(f"{ctx.author.id} has reported the following bug:\n`{bug}`")
      await ctx.send("I have successfully reported that bug to Geb!")
    
  @commands.command()
  @commands.guild_only()
  async def feedback(self, ctx, *, feedback):
    if ctx.author.id == None:
      return
    else:
      owner = self.client.get_user(660563979684544513)
      await owner.send(f"{ctx.author.id} has given this feedback:\n`{feedback}`")
      await ctx.send("Thanks for your feedback!")
    
    
    
      
def setup(client):
  client.add_cog(randomCog(client))