from discord.ext import commands

config = {}
with open("CONFIG.txt") as f:
    for line in f:
        if "=" in line:
            k, v = line.strip().split("=", 1)
            config[k] = v.strip('"').strip("'").strip()

class Paypal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pp(self, ctx):
        await ctx.send(config["PAYPAL_EMAIL"])

async def setup(bot):
    await bot.add_cog(Paypal(bot))
