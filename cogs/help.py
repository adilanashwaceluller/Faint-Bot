import discord
from discord.ext import commands


class helpCog(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  @commands.guild_only()
  async def help(self, ctx):
      embed = discord.Embed(description=f"Servers - {len(self.client.guilds)}\nDev - Geb#0420\nInvite - [Click here](https://discord.com/api/oauth2/authorize?client_id=870984698007007242&permissions=8&scope=bot%20applications.commands)\n", color=0x2f3136)
      embed.set_author(name="Faint")
      embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
      embed.add_field(name=f"Moderation", value=f"`ban`, `kick`, `modnick`, `nick`, `nuke`, `slowmode`, `unban`, `unbanall`, `nuke`, `nick`", inline=False)
      embed.add_field(name=f"Utility", value=f"`av`, `afk`, `poll`, `coinflip`, `nuke`, `add`, `subtract`, `times`, `divide`", inline=False)
      embed.add_field(name=f"Fun", value=f"`pp`, `repeat`, `repeatembed`, `wizz`, `coinflip`")
      embed.add_field(name=f"Information", value=f"`botinfo`, `ping`, `invite`, `credits`, `reportbug`, `feedback`", inline=False)
      embed.set_footer(text = f"Faint  |  Developed by Geb")
      await ctx.reply(embed=embed)
    
def setup(client):
  client.add_cog(helpCog(client))