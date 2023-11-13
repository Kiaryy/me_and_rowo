import os
import discord
from discord.ext import commands
from random import randint
from secret import secret
# Create an instance of the bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def count_files_in_folder(folder_path): # Gets the number of files in a folder
    try:
        # List all files in the directory
        files = os.listdir(folder_path)

        # Use a list comprehension to filter out non-files
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]

        # Get the count of files
        file_count = len(files)

        return file_count

    except FileNotFoundError:
        print(f"The folder '{folder_path}' was not found.")
        return None

def change_name_files(folder_path):
        # List all files in the directory
        files = os.listdir(folder_path)
        # Use a list comprehension to filter out non-files
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
        
        i = 0
        try: 
            for file in files:
                if file != f"{i}.gif":
                    os.rename(f"{folder_path}/{file}", f"{folder_path}/{i}.gif")
                i +=1
        except FileExistsError:
            print(f"All the files in {folder_path} have the correct name")

shrimple_lenght = count_files_in_folder("shrimple_gifs")

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
    change_name_files("shrimple_gifs")

# Command: !hello
@bot.command(name='shrimple')
async def hello(ctx):
    await ctx.send(file=discord.File(f'shrimple_gifs/{randint(0,shrimple_lenght-1)}.gif'))

# Run the bot
bot.run(secret)
