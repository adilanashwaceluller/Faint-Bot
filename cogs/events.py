import discord
from discord.ext import commands


class EventsCog(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.Cog.listener()
  async def on_message(self, message):
    
    if message.author == self.client.user:
      return
    
    if message.author.bot: 
      return
    
    if message.content.startswith(f"<@!{self.client.user.id}>") and len(message.content) == len(f"<@!{self.client.user.id}>"):
      embed=discord.Embed(description="My prefix is `;`", color=0x2f3136)
      await message.channel.send(embed=embed)
      
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    
    if isinstance(error, commands.CommandOnCooldown):
            embed=discord.Embed(description=f"<:error:893524963691200573> You are currently on cooldown, try again in {round(error.retry_after, 1)} seconds!\n<:support:893525031836074014> Click [**here**](https://discord.gg/QY26JtTE2y) for support!", color=0x2f3136)
            await ctx.send(embed=embed)
            
    elif isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description=f"<:error:893524963691200573> You are missing required permission(s) to use this command!\n<:support:893525031836074014> Click [**here**](https://discord.gg/QY26JtTE2y) for support!", color=0x2f3136)
            await ctx.send(embed=embed)
            
    elif isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(description=f"<:error:893524963691200573> You are missing required argument(s) to use this command!\n<:support:893525031836074014> Click [**here**](https://discord.gg/QY26JtTE2y) for support!", color=0x2f3136)
            await ctx.send(embed=embed)
              
  @commands.Cog.listener()
  async def on_member_join(self, member: discord.Member):
    try:
      # if you want to dm a member on join you can do it here ( eg. await member.send("Welcome!") )
      return
    except:
        return
      
 

    


def setup(client):
  client.add_cog(EventsCog(client))