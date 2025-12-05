from discord.ext import commands
import pyfiglet

class Ascii(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ascii(self, ctx, *, message=None):
        if not message:
            await ctx.send(f"❌ Invalid command.`\n> __Command__: `ascii <message>`", delete_after=5)
            return
        try:
            ascii_art = pyfiglet.figlet_format(message)
            await ctx.send(f"```\n{ascii_art}\n```", delete_after=5)
        except Exception as e:
            await ctx.send(f"❌ An error occurred while generating the ASCII art. `{e}`", delete_after=5)

async def setup(bot):
    await bot.add_cog(Ascii(bot))