##nextcordをインポート
import nextcord
from nextcord.ext import commands
from colorama import Fore
import json

import webserver
##config.jsonを読み込み
with open('config.json','r') as f:
  config = json.load(f)

##Botの設定
intents = nextcord.Intents.all()
intents.message_content = True
intents.typing = False
bot = commands.Bot(
##Botのprefixの設定
  command_prefix=config['prefix'],
##デフォルトのhelp削除
  help_command=None,
  intents=intents
)
##Botの起動時のコンソール出力
@bot.event
async def on_ready():
  print(Fore.GREEN + f"正常に起動しました:{bot.user}" + Fore.GREEN)
  await bot.change_presence(activity=nextcord.Game(name=f"{config['prefix']}help"))
##Botのコマンド(!kon)
@bot.command()
async def help(ctx):
  embed=nextcord.Embed(title="help",description=f"{config['prefix']}help helpを表示する/n{config['prefix']}kon こんにちは！と返す")
  await ctx.send(embed=embed)
##Botのコマンド(!kon)
@bot.command()
async def kon(ctx):
  await ctx.send("こんにちは！")
##Botのslashコマンド(/konn)
@nextcord.slash_command(description="こんにちは！と返してくれる")
async def konn(ctx):
  await ctx.send("こんにちは！")
  
##webserverの起動
webserver.start()
##botの起動
bot.run(config['token'])