from discord.ext import commands
import discord

config = {}
with open("CONFIG.txt") as f:
    for line in f:
        if "=" in line:
            k, v = line.strip().split("=", 1)
            config[k] = v.strip('"').strip("'").strip()

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_message = None
        self.is_afk = False

    @commands.command()
    async def afk(self, ctx, *, reason=None):
        if not self.is_afk:
            self.afk_message = reason if reason else config.get("AFK_MESSAGE_DEFAULT")
            self.is_afk = True
            await ctx.send(f"`💤 You are now AFK: {self.afk_message}`", delete_after=5)
        else:
            self.is_afk = False
            self.afk_message = None
            await ctx.send("`✅ AFK status removed.`", delete_after=5)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

        if self.is_afk and isinstance(message.channel, discord.DMChannel):
            try:
                await message.channel.send(f"`💤 I'm currently AFK: {self.afk_message}`", delete_after=15)
            except Exception as e:
                print(f"`[AFK] Error replying to message: {e}`")

async def setup(bot):
    await bot.add_cog(AFK(bot))