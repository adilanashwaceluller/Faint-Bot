import discord
from discord.ext import commands
import asyncio

class MathCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.guild_only()
  async def add(self, ctx, num1: float, num2: float):
    await ctx.send(f"The sum of these numbers is **{num1+num2}**")

  @commands.command()
  @commands.guild_only()
  async def subtract(self, ctx, num1: float, num2: float):
    await ctx.send(f"The sum of these numbers is **{num1-num2}**")

  @commands.command()
  @commands.guild_only()
  async def times(self, ctx, num1: float, num2: float):
    await ctx.send(f"The sum of these numbers is **{num1*num2}**")

  @commands.command()
  @commands.guild_only()
  async def divide(self, ctx, num1: float, num2: float):
    await ctx.send(f"The sum of these numbers is **{num1/num2}**")

  @commands.command()
  @commands.guild_only()
  async def math(self, ctx):
    await ctx.send(f";add [number] [number]\n;subtract [number] [number]\n;times [number] [number]\n;divide [number] [number]")
  
  @commands.command()
  @commands.guild_only()
  async def calculate(self, ctx, num1: float, method, num2: float):
    if num1 and method and num2 is None:
      await ctx.send("Wrong usage\n`;calculate [number] [method] [number]`")
    if method == '+':
      await ctx.send(f"Answer to {num1} plus {num2}:\n**{num1+num2}**")
      return
    if method == '-':
      await ctx.send(f"Answer to {num1} minus {num2}:\n**{num1-num2}**")
      return
    if method == '/':
      await ctx.send(f"Answer to {num1} divide {num2}:\n**{num1/num2}**")
      return
    if method == '*':
      await ctx.send(f"Answer to {num1} times {num2}:\n**{num1*num2}**")
      return
    else:
      await ctx.send(f"{method} is not a valid input, please choose one of the following: `+` , `-` , `*` , `/` ")

  

def setup(client):
  client.add_cog(MathCog(client))