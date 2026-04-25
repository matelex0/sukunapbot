from discord.ext import commands

class AvatarBanner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, user: commands.UserConverter = None):
        user = user or ctx.author
        if user.avatar:
            await ctx.send(user.avatar.url)
        else:
            await ctx.send("`❌ This user doesn't have an avatar.`", delete_after=5)

async def setup(bot):
    await bot.add_cog(AvatarBanner(bot))