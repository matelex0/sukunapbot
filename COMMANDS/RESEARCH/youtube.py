from discord.ext import commands
import requests

class YouTubeSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="yt")
    async def youtube(self, ctx, *, query):
        r = requests.get(f"https://noembed.com/embed?url=https://www.youtube.com/results?search_query={query}")
        await ctx.send(f"`🔍 Search on Youtube:` **{query}\nhttps://www.youtube.com/results?search_query={query}**")

async def setup(bot):
    await bot.add_cog(YouTubeSearch(bot))
