from discord.ext import commands
import discord
from dotenv import load_dotenv
import traceback

from .env.keys.env import TOKEN

intents = discord.Intents.all()

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents)
        self.exts = [
            'cogs.others',
            # 'cogs.itudoko',
            # 'cogs.point',
            # 'cogs.hogestory',
            # 'cogs.superchat',
            # 'cogs.help',
            'cogs.todo',
            'cogs.shogi',
            # 'cogs.nb',
            # 'cogs.keiba',
            # 'cogs.stat',
            # 'cogs.timer',
            # 'cogs.talk',
            # 'cogs.genshin',
            # 'cogs.test'
        ]

    async def on_ready(self):
        print(f"{self.user} On ready.")
        for ext in self.exts:
            await self.load_extension(ext)
        commands = await bot.tree.sync()
        command_log = ",".join(command.name for command in commands)
        print(command_log)

if __name__ == "__main__":
    bot = MyBot()
    bot.run(TOKEN)
