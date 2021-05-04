#加入的物件功能
import discord
from discord.ext import commands
import json
import random
import os

#開啟資料夾內的json檔案
with open('setting.json','r',encoding='utf8')as jfile:
   jdata = json.load(jfile)
#呼叫機器人指令設定
intents=discord.Intents.all()
bot = commands.Bot(command_prefix= '*', intents=intents)
#成員功能設定賦予
client = discord.Client(intents=intents)
#叫機器人上線成功給予的訊息
@bot.event
async def on_ready():
  print(">> 康羿進入了頻道 <<")

@bot.command()
async def load(ctx, extension):
   bot.load_extension(f'cmds.{extension}')
   await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
   bot.unload_extension(f'cmds.{extension}')
   await ctx.send(f'Un - Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
   bot.reload_extension(f'cmds.{extension}')
   await ctx.send(f'Re - Loaded {extension} done.')

#引進bot資料夾內的cmds
for Filename in os.listdir('./cmds'):
   #只有副檔名事.py的才執行
   if Filename.endswith('.py'):
      #不顯示檔名後三字元
       bot.load_extension(F'cmds.{Filename[:-3]}')
#篩選顯示
if __name__ == "__main__":
#執行的機器人
   bot.run(jdata['TOKEN'])
 