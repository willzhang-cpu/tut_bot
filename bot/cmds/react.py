import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

#開啟資料夾內的json檔案
with open('setting.json','r',encoding='utf8')as jfile:
   jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 隨機圖片(selF,ctx):
       random_pic = random.choice(jdata['pic'])
       pic = discord.File(random_pic)
       await ctx.send(file= pic)
#傳送我的老婆圖片
    @commands.command()
    async def 康羿的老婆(selF,ctx):
       pic = discord.File(jdata['wife'])
       await ctx.send(file= pic)

def setup(bot):
   bot.add_cog(React(bot))  