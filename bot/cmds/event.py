import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

#開啟資料夾內的json檔案
with open('setting.json','r',encoding='utf8')as jfile:
   jdata = json.load(jfile)

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
       channel = self.bot.get_channel(int(jdata['Welcome_channel']))
       await channel.send(f'{member} 歡迎加入醒吾,老司機上車啦! ')

    @commands.Cog.listener()   
    async def on_member_remove(self,member):
       channel = self.bot.get_channel(int(jdata['Leave_channel']))
       await channel.send(f'{member} 離開讓我們默哀3秒!') 

    @commands.Cog.listener()
    async def on_message(self, msg):
      if msg.content.endswith('ahoy'):
          await msg.channel.send('厄~~是臭DD')

def setup(bot):
   bot.add_cog(event(bot))