from discord.ext import commands

class WebSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="web")
    async def web_search(self, ctx, *, query):
        await ctx.send(f"`🔎 Search on Google:` **https://www.google.com/search?q={query.replace(' ', '+')}**")

async def setup(bot):
    await bot.add_cog(WebSearch(bot))
