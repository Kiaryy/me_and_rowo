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
cars = files_in_folder("silly_cars")
# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print("Ready to do some tomfoolery")
    print('------')

# Command: !shrimple
@bot.command(name='shrimple')
async def hello(ctx):
    await ctx.send(file=discord.File(f'shrimple_gifs/{shrimple[1][randint(0,shrimple[0]-1)]}'))

# Command: !cars
@bot.command(name='cars')
async def hello(ctx):
    await ctx.send(file=discord.File(f'silly_cars/{cars[1][randint(0,cars[0]-1)]}'))

# Command: !hello
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Haiiii :3')
    await ctx.send('https://tenor.com/view/crab-wave-greetings-hi-hello-gif-7698888542717415913')

# Command: !roll_D6
@bot.command(name='roll_D6')
async def guess(ctx):
    number = randint(1, 6)
    await ctx.send(number)

# Command: !guess_the_number
@bot.command(name='guess')
async def guess(ctx):
    number = randint(1, 10)
    await ctx.send(number)

# Run the bot
bot.run(secret)