import re
import discord
import discord.ext.commands as commands
from copypasta import the_true

token = "A valid token"
bot = commands.Bot(command_prefix=None)
triggers = ("pipi", "petrosyan", "petrosian", "tigran", "pampers",
            "firouzja", "true", "fair", "lier", "proffesional", "crying babe")
pattern = re.compile(f'({"|".join(triggers)})', flags=re.I)


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user or re.search(pattern, message.content) is None:
        return
    await message.channel.send(the_true)

bot.run(token)
