from discord.ext import commands

class ToS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tos(self, ctx, option=None):
        if option is None:
            await ctx.message.delete()
            await ctx.send("`❓ Usage: .tos [pp/ltc]`")
            return
            
        if option.lower() == "pp":
            await ctx.message.delete()
            await ctx.send("🔒 **Privacy Policy**\nBy using this selfbot, you acknowledge and agree that your data may be collected and used in accordance with Discord's Terms of Service.")
        
        elif option.lower() == "ltc":
            await ctx.message.delete()
            await ctx.send("📜 **Legal Terms & Conditions**\nThis selfbot is for educational purposes only. Users are responsible for complying with Discord's Terms of Service. Use at your own risk.")
        
        else:
            await ctx.message.delete()
            await ctx.send("`❌ Invalid option. Use .tos pp or .tos ltc`")

async def setup(bot):
    await bot.add_cog(ToS(bot))