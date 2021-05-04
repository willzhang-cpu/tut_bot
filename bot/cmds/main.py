import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
   
   #我的傳送ping值
   @commands.command()
   async def ping(self,ctx):
     await ctx.send(F'{round(selF.bot.latency*1000)} (ms)')       

   @commands.command()
   async def 康羿(selF,ctx):
    await ctx.send('有什麼事情?')

def setup(bot):
   bot.add_cog(Main(bot))  