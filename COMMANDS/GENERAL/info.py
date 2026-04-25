from discord.ext import commands
import platform
import psutil
import time
import sys
import subprocess
import discord

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()
        self.bot_version = "1.0.0"
        try:
            result = subprocess.run(["git", "describe", "--tags", "--always"], capture_output=True, text=True, timeout=3)
            self.bot_version = result.stdout.strip() or "1.0.0"
        except:
            pass

    def get_uptime(self):
        uptime = time.time() - self.start_time
        days = int(uptime // 86400)
        hours = int((uptime % 86400) // 3600)
        minutes = int((uptime % 3600) // 60)
        return days, hours, minutes

    def get_network(self):
        net = psutil.net_io_counters()
        return net.bytes_sent, net.bytes_recv

    @commands.command()
    async def info(self, ctx):
        days, hours, minutes = self.get_uptime()
        cpu_usage = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        net_sent, net_recv = self.get_network()

        info_text = f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```👑 Creator```
• **Created by Matelex**
```📱 Discord```
• **Contact: matelex.it**
```🤖 Bot```
• **Version: {self.bot_version}**
• **Python: {sys.version.split()[0]}**
• **discord.py: {discord.__version__}**
```💻 System```
• **OS: {platform.system()} {platform.release()}**
• **CPU Usage: {cpu_usage}%**
• **RAM Usage: {memory.percent}%**
• **Disk Usage: {disk.percent}%**
• **Network: ↓{self.format_bytes(net_recv)} ↑{self.format_bytes(net_sent)}**
```⏰ Uptime```
• **{days}d {hours}h {minutes}m**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
*Thanks for using my selfbot!* 💖
"""
        await ctx.send(info_text)

    def format_bytes(self, bytes_val):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.1f}{unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.1f}PB"

async def setup(bot):
    await bot.add_cog(Info(bot))