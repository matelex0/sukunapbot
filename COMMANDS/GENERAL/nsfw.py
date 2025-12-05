from discord.ext import commands
import requests

config = {}
with open("CONFIG.txt") as f:
    for line in f:
        if "=" in line:
            k, v = line.strip().split("=", 1)
            config[k] = v.strip('"').strip("'").strip()

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nsfw")
    async def nsfw(self, ctx, category=None):
        categories = ["Anal", "Ass", "Boobs", "Gonewild", "Hanal", "Hass", "Hboobs", "Hentai", "Hkitsune", "Hmidriff", "Hneko", "Hthigh", "Neko", "Paizuri", "Pgif", "Pussy", "Tentacle", "Thigh", "Yaoi"]
        
        if category is None:
            categories_str = "\n".join([f"{cat}" for cat in categories])
            await ctx.send(f"## Categories:\n\n**```{categories_str}```**", delete_after=30)
            return

        headers = {
            "authorization": (config["NSFW_KEY"])
        }
        res = requests.get(f"https://api.night-api.com/images/nsfw/{category}", headers=headers)
        data = res.json()
        await ctx.send(data["content"]["url"])

async def setup(bot):
    await bot.add_cog(NSFW(bot))