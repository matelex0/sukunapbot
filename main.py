from discord.ext import commands
import os
import asyncio

# CONFIG LOAD
config = {}
with open("CONFIG.txt") as f:
    for line in f:
        if "=" in line:
            k, v = line.strip().split("=", 1)
            config[k] = v.strip('"').strip("'").strip()

# ASCII BANNER
def print_ascii_banner(user_id):
    ascii_art = r"""
   _____       _                         _____  ____        _   
  / ____|     | |                       |  __ \|  _ \      | |  
 | (___  _   _| | ___   _ _ __   __ _   | |__) | |_) | ___ | |_ 
  \___ \| | | | |/ / | | | '_ \ / _` |  |  ___/|  _ < / _ \| __|
  ____) | |_| |   <| |_| | | | | (_| |  | |    | |_) | (_) | |_ 
 |_____/ \__,_|_|\_\\__,_|_| |_|\__,_|  |_|    |____/ \___/ \__|

"""
    print(ascii_art)
    print(f"👤 UserID  : {user_id}")
    print("🙏 Thank you for using SukunaPBot!\n")

# CHANGE PREFIX IF YOU NEED, I WILL ADD IT IN CONFIG.txt IN THE NEXT UPDATES!
bot = commands.Bot(command_prefix=".", self_bot=True)
bot.help_command = None
@bot.event
async def on_command(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

async def load_extensions():
    for category in os.listdir("COMMANDS"):
        category_path = os.path.join("COMMANDS", category)
        if os.path.isdir(category_path):
            for file in os.listdir(category_path):
                if file.endswith(".py") and file != "__init__.py":
                    extension = f"COMMANDS.{category}.{file[:-3]}"
                    try:
                        await bot.load_extension(extension)
                        print(f"🔹 Loaded extension: {extension}")
                    except Exception as e:
                        print(f"[❌] Error loading extension {extension}: {e}")

async def main():
    async with bot:
        try:
            await bot.login(config["TOKEN"])
        except Exception as e:
            print(f"[❌] Login error: {e}")
            return
        print_ascii_banner(bot.user.id)
        await load_extensions()
        try:
            await bot.connect()
        except Exception as e:
            print(f"[❌] Error connecting to the bot: {e}")
try:
    asyncio.run(main())
except Exception as e:
    print(f"[❌] Critical error in bot execution: {e}")
