import discord
from discord.ext import commands
import time
import aiohttp

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = None

    async def cog_load(self):
        self.session = aiohttp.ClientSession()
    
    async def cog_unload(self):
        if self.session:
            await self.session.close()

    @commands.command()
    async def ping(self, ctx):
        start = time.perf_counter()
        
        latency = round(self.bot.latency * 1000)
        
        try:
            async with self.session.get("https://discord.com/api/v10/gateway") as resp:
                if resp.status == 200:
                    api_latency = int((time.perf_counter() - start) * 1000)
                else:
                    api_latency = "N/A"
        except:
            api_latency = "ERR"
        
        await ctx.send(f"""
```
🏓 PING
━━━━━━━━━━━━━━━━━━━
🌐 API Latency: {latency}ms
📡 HTTP Latency: {api_latency}ms
━━━━━━━━━━━━━━━━━━━
⚡ Total: {latency + (api_latency if isinstance(api_latency, int) else 0)}ms
```
""", delete_after=10)

async def setup(bot):
    await bot.add_cog(Ping(bot))