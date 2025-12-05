from discord.ext import commands
import aiohttp

class Converter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"

    async def get_exchange_rate(self, from_currency: str, to_currency: str) -> float:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_url}{from_currency}") as response:
                data = await response.json()
                return data["rates"][to_currency]

    @commands.command(name="exchange")
    async def exchange(self, ctx, from_currency: str, to_currency: str, amount: float):
        try:
            from_currency = from_currency.upper()
            to_currency = to_currency.upper()
            rate = await self.get_exchange_rate(from_currency, to_currency)
            converted = round(amount * rate, 2)
            await ctx.send(f"**Exchange:**\n> `💱 {amount} {from_currency} ≈ {converted} {to_currency} 💰`", delete_after=5)
        except KeyError:
            await ctx.send("`❌ Invalid currency. Please use international currency codes (e.g. EUR, USD, GBP)`", delete_after=5)
        except Exception as e:
            await ctx.send("`⚠️ An error occurred during the conversion.`", delete_after=5)

async def setup(bot):
    await bot.add_cog(Converter(bot))