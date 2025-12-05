from discord.ext import commands
import random
import string

class FakeNitro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nitro(self, ctx):
        await ctx.message.delete()
        code = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
        await ctx.send(f"**Discord Nitro**\nHere is your free Nitro gift!\nhttps://discord.gift/{code}", delete_after=10)

async def setup(bot):
    await bot.add_cog(FakeNitro(bot))