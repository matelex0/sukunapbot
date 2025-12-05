import requests
from discord.ext import commands

class TokenChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def checktoken(self, ctx, token):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }

        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            message = "**✅ Valid Token**\n\n"
            message += f"👤 **Username:** {user_data['username']}#{user_data['discriminator']}\n"
            message += f"🆔 **ID:** {user_data.get('id', 'None')}\n"
            message += f"📧 **Email:** {user_data.get('email', 'None')}\n"
            message += f"📱 **Phone:** {user_data.get('phone', 'None')}\n"
            message += f"🔐 **2FA Enabled:** {str(user_data.get('mfa_enabled', False))}\n"
            message += f"✔️ **Verified:** {str(user_data.get('verified', False))}\n"
            message += f"🌍 **Locale:** {user_data.get('locale', 'None')}\n"
            message += f"💎 **Nitro Type:** {user_data.get('premium_type', 'None')}\n"
            message += f"🖼️ **Avatar Hash:** {user_data.get('avatar', 'None')}\n"
            message += f"🎨 **Banner Hash:** {user_data.get('banner', 'None')}\n"
            message += f"📝 **Bio:** {user_data.get('bio', 'None')}"
            await ctx.send(message)
        else:
            await ctx.send("**❌ Invalid Token**", delete_after=5)

async def setup(bot):
    await bot.add_cog(TokenChecker(bot))