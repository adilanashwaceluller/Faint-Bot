import discord
from discord.ext import commands


class MessageCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.guild_only()
  async def repeat(self, ctx, *, message: str = None):
    if message is None:
      await ctx.send('What do you want me to say?')
      def check(m):
        return m.author.id == ctx.author.id

      message = await self.client.wait_for('message', check=check)
      await ctx.send(f"{message.content}")

    else:
      await ctx.send(f"{message}")

  @commands.command()
  @commands.guild_only()
  async def repeatembed(self, ctx, *, message: str = None):
    if message is None:
      await ctx.send('What do you want me to say?')
      def check(m):
        return m.author.id == ctx.author.id

      message = await self.client.wait_for('message', check=check)
      embed=discord.Embed(description=f"{message.content}", color=0x2f3136)
      await ctx.send(embed=embed)

    else:
      embed=discord.Embed(description=f"{message}", color=0x2f3136)
      await ctx.send(embed=embed)

  @commands.command() 
  @commands.guild_only()
  async def poll(self, ctx, *, poll=None):
      if poll == None:
        await ctx.send("Please Specify A Question")
      else:
        embed = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} Asks:",description = poll, color=0x2f3136)
        message = await ctx.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")


    




def setup(client):
  client.add_cog(MessageCog(client))