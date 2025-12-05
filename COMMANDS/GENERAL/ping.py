import discord
from discord.ext import commands
import time

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("`Pong!`")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"`Pong! {int(ping)}ms`", delete_after=5)

async def setup(bot):
    await bot.add_cog(Ping(bot))
