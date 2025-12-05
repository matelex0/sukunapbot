from discord.ext import commands
import discord

config = {}
with open("CONFIG.txt") as f:
    for line in f:
        if "=" in line:
            k, v = line.strip().split("=", 1)
            config[k] = v.strip('"').strip("'").strip()

class AutoResponder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.enabled = False 

    @commands.command()
    async def autoreply(self, ctx, state: str = None):
        await ctx.send("`⚠️ This feature is currently under maintenance. Please try again later.`", delete_after=5)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user or not self.enabled:
            return

        if self.bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
            await message.channel.send("`⚠️ This feature is currently under maintenance. Please try again later.`", delete_after=5)

async def setup(bot):
    await bot.add_cog(AutoResponder(bot))