import discord
import discord.ext.commands as commands
import copypasta

token = "A valid token"
bot = commands.Bot(command_prefix=None)
triggers = ["pipi", "petrosyan", "petrosian", "tigran", "pampers", "firouzja", "true", "fair", "lier", "proffesional", "crying babe"]


@bot.event
async def on_message(message):
    if message.author == bot.user: return
    message.content = message.content.lower()
    for i in triggers:
        if i in message.content:
            await message.channel.send(copypasta.messageable)
            break

bot.run(token)
