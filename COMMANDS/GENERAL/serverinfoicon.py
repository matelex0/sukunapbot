from discord.ext import commands
import discord

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        g = ctx.guild
        server_info = (
            "```📘 SERVER INFORMATION 📘```\n\n"
            f"> **Name:** {g.name}\n"
            f"> **Members:** {g.member_count}\n"
            f"> **Owner:** {g.owner}\n"
            f"> **ID:** {g.id}\n"
            f"> **Created At:** {g.created_at.strftime('%d/%m/%Y')}\n"
            f"> **Boost Level:** {g.premium_tier}\n"
            f"> **Roles:** {len(g.roles)}\n"
            f"> **Channels:** {len(g.channels)}\n\n"
        )
        await ctx.send(server_info)

    @commands.command()
    async def servericon(self, ctx):
        icon_url = ctx.guild.icon.url if ctx.guild.icon else "Server has no icon"
        if isinstance(icon_url, str):
            await ctx.send(icon_url)
        else:
            embed = discord.Embed(title=f"{ctx.guild.name}'s Icon")
            embed.set_image(url=icon_url)
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ServerInfo(bot))