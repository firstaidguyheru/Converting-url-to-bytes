import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO
import requests

load_dotenv()

client = commands.Bot(command_prefix='-', help_command=None)

@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')


@client.command()
async def p(ctx):
    url = ctx.guild.icon_url
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    b = BytesIO()
    img.save(b, format='JPEG')
    byte_im = b.getvalue()
    print(byte_im)

client.run(os.getenv('TOKEN'))
