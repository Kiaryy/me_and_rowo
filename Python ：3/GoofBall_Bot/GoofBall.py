import os
import discord
from discord.ext import commands
from random import randint
from secret import secret
# Create an instance of the bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def files_in_folder(folder_path): # Gives the number of files in a folder, and a list with all the files
    try:
        # List all files in the directory
        files = os.listdir(folder_path)
        
        # Use a list comprehension to filter out non-files
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
        
        # Get the count of files
        file_count = len(files)
        
        return (file_count, files)
    except FileNotFoundError:
        print(f"The folder '{folder_path}' was not found.")
        return None


shrimple = files_in_folder("shrimple_gifs")

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print("Ready to do some tomfoolery")
    print('------')

# Command: !hello
@bot.command(name='shrimple')
async def hello(ctx):
    await ctx.send(file=discord.File(f'shrimple_gifs/{shrimple[1][randint(0,shrimple[0]-1)]}'))

# Run the bot
bot.run(secret)
