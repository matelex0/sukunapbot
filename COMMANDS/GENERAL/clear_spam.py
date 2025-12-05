from discord.ext import commands

class ClearSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: int = 10):
         deleted = 0
         async for msg in ctx.channel.history(limit=amount):
           if msg.author == self.bot.user:
            try:
                await msg.delete()
                deleted += 1
            except Exception as e:
                print(f"Error: {e}")
                await ctx.send(f"🧹 I deleted {deleted} your texts.", delete_after=5)


    @commands.command()
    async def spam(self, ctx, *, msg):
        for _ in range(5):
            await ctx.send(msg)

    @commands.command()
    async def spamreact(self, ctx, emoji: str):
        async for msg in ctx.channel.history(limit=5):
            await msg.add_reaction(emoji)

async def setup(bot):
    await bot.add_cog(ClearSpam(bot))
