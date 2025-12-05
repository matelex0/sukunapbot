from discord.ext import commands
import requests

class MemeJoke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        r = requests.get("https://api.imgflip.com/get_memes")
        memes = r.json()
        if memes["success"]:
            import random
            meme = random.choice(memes["data"]["memes"])
            await ctx.send(meme["url"], delete_after=8)

    @commands.command()
    async def joke(self, ctx):
        r = requests.get("https://v2.jokeapi.dev/joke/Any?lang=en")
        joke = r.json()
        if joke["type"] == "single":
            await ctx.send(joke["joke"])
        else:
            await ctx.send(f"{joke['setup']}\n{joke['delivery']}", delete_after=12)

async def setup(bot):
    await bot.add_cog(MemeJoke(bot))