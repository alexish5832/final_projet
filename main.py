import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user}')
    print(f'')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment. filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send("мусор на вашей фотографии принадлежит к:")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Вы забыли загрузить картинку :(")

bot.run("TOKEN")
