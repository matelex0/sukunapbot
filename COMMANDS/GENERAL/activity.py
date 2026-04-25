from discord.ext import commands
import discord

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def playing(self, ctx, *, text):
        try:
            await self.bot.change_presence(activity=discord.Game(name=text))
            await ctx.send(f"`✅ Playing: {text}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error: {e}`", delete_after=5)

    @commands.command()
    async def listening(self, ctx, *, text):
        try:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))
            await ctx.send(f"`✅ Listening: {text}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error: {e}`", delete_after=5)

    @commands.command()
    async def watching(self, ctx, *, text):
        try:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))
            await ctx.send(f"`✅ Watching: {text}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error: {e}`", delete_after=5)

    @commands.command()
    async def stream(self, ctx, url: str = None, *, text=None):
        text = text or "Live"
        url = url or "https://www.twitch.tv/matelex"
        try:
            await self.bot.change_presence(activity=discord.Streaming(name=text, url=url))
            await ctx.send(f"`✅ Streaming: {text}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error: {e}`", delete_after=5)

    @commands.command()
    async def cactivity(self, ctx):
        try:
            await self.bot.change_presence(status=discord.Status.online, activity=None)
            await ctx.send("`✅ Status cleared`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error: {e}`", delete_after=5)

    @commands.command()
    async def setstatus(self, ctx, status_type: str):
        status_types = {
            "online": discord.Status.online,
            "idle": discord.Status.idle,
            "dnd": discord.Status.dnd,
            "invisible": discord.Status.invisible,
            "dnd_only": "do_not_disturb"
        }
        if status_type.lower() not in status_types:
            await ctx.send("`❌ Use: online, idle, dnd, invisible`", delete_after=5)
            return
        try:
            await self.bot.change_presence(status=status_types[status_type.lower()])
            await ctx.send(f"`✅ Status: {status_type}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Error: {e}`", delete_after=5)

async def setup(bot):
    await bot.add_cog(Status(bot))