from discord.ext import commands
import discord

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        g = ctx.guild
        
        bots = sum(1 for m in g.members if m.bot)
        humans = g.member_count - bots
        
        emojis = len(g.emojis)
        stickers = len(g.stickers)
        
        embed = discord.Embed(color=0x2f3136)
        embed.set_author(name=g.name, icon_url=g.icon.url if g.icon else None)
        embed.add_field(name="📊 Members", value=f"Total: {g.member_count}\nHumans: {humans}\nBots: {bots}", inline=True)
        embed.add_field(name="📅 Created", value=g.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="👑 Owner", value=g.owner, inline=True)
        embed.add_field(name="🛡️ Verification", value=g.verification_level.name.title(), inline=True)
        embed.add_field(name="⭐ Boost Level", value=f"Tier {g.premium_tier}", inline=True)
        embed.add_field(name="🔢 Roles", value=len(g.roles), inline=True)
        embed.add_field(name="😀 Emojis", value=f"{emojis}/{g.emoji_limit}", inline=True)
        
        text_channels = len([c for c in g.channels if isinstance(c, discord.TextChannel)])
        voice_channels = len([c for c in g.channels if isinstance(c, discord.VoiceChannel)])
        embed.add_field(name="📢 Channels", value=f"Text: {text_channels}\nVoice: {voice_channels}", inline=True)
        
        if g.icon:
            embed.set_thumbnail(url=g.icon.url)
        
        await ctx.send(embed=embed)

    @commands.command()
    async def servericon(self, ctx):
        if not ctx.guild.icon:
            await ctx.send("`❌ Server has no icon`", delete_after=5)
            return
        
        embed = discord.Embed(title=f"{ctx.guild.name}'s Icon")
        embed.set_image(url=ctx.guild.icon.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ServerInfo(bot))