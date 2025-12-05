from discord.ext import commands
import platform
import psutil
import time

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command()
    async def info(self, ctx):
        uptime = time.time() - self.start_time
        hours = int(uptime // 3600)
        minutes = int((uptime % 3600) // 60)
        
        cpu_usage = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        
        info_text = f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```👑 Creator```
• **Created by Alexone**
```📱 Discord```
• **Contact: idiozia**
```💻 System```
• **OS: {platform.system()}** 🖥️
• **CPU Usage: {cpu_usage}%** ⚡
• **RAM Usage: {memory.percent}%** 📊
```⏰ Uptime```
• **{hours}h {minutes}m**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
*Thanks for using my selfbot!* 💖
"""
        await ctx.send(info_text)

async def setup(bot):
    await bot.add_cog(Info(bot))