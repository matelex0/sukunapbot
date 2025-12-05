from discord.ext import commands
import discord

config = {}
with open("CONFIG.txt") as f:
    for line in f:
        if "=" in line:
            k, v = line.strip().split("=", 1)
            config[k] = v.strip('"').strip("'").strip()

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def playing(self, ctx, *, text):
        try:
            await self.bot.change_presence(activity=discord.Game(name=text))
            await ctx.send(f"`✅ Playing status set to: {text}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error setting game status: {e}`", delete_after=5)

    @commands.command()
    async def stream(self, ctx, *, text):
        try:
            await self.bot.change_presence(activity=discord.Streaming(name=text, url="https://www.twitch.tv/alexontoppe"))
            await ctx.send(f"`✅ Streaming status set to: {text}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error setting stream status: {e}`", delete_after=5)

    @commands.command()
    async def cactivity(self, ctx):
        try:
            await self.bot.change_presence(status=discord.Status.online, activity=None)
            await ctx.send("`✅ Status has been cleared`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error clearing status: {e}`", delete_after=5)

    @commands.command()
    async def setstatus(self, ctx, status_type: str, *, text=None):
        try:
            status_types = {
                "online": discord.Status.online,
                "idle": discord.Status.idle,
                "dnd": discord.Status.dnd,
                "invisible": discord.Status.invisible
            }
            if status_type.lower() not in status_types:
                await ctx.send("`❌ Invalid status type. Use: online, idle, dnd, or invisible`", delete_after=5)
                return
            
            await self.bot.change_presence(status=status_types[status_type.lower()])
            await ctx.send(f"`✅ Status set to: {status_type}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error setting status: {e}`", delete_after=5)

async def setup(bot):
    await bot.add_cog(Status(bot))