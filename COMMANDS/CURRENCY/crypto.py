from discord.ext import commands
import requests

class Crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cryptoeur(self, ctx, coin: str):
        try:
            url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&ids={coin}"
            response = requests.get(url, timeout=10).json()
            if not response:
                await ctx.send("`❌ Crypto not found!`", delete_after=5)
                return
            
            data = response[0]
            price = data["current_price"]
            change = data["price_change_percentage_24h"]
            market_cap = data["market_cap"]
            volume = data["total_volume"]
            rank = data["market_cap_rank"]
            
            icon = "📈" if change >= 0 else "📉"
            change_str = f"+{change:.2f}%" if change >= 0 else f"{change:.2f}%"
            
            await ctx.send(f"""
```
💎 {data["name"]} ({data["symbol"].upper()})
━━━━━━━━━━━━━━━━━━━━━━
💰 Prezzo: {price:,.2f} EUR
{icon} 24h: {change_str}
📊 Market Cap: {self.format_num(market_cap)} EUR
📈 Volume: {self.format_num(volume)} EUR
🏆 Rank: #{rank}
```
""", delete_after=15)
        except Exception as e:
            await ctx.send(f"`❌ Errore: {str(e)}`", delete_after=5)

    @commands.command()
    async def cryptousd(self, ctx, coin: str):
        try:
            url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin}"
            response = requests.get(url, timeout=10).json()
            if not response:
                await ctx.send("`❌ Crypto not found!`", delete_after=5)
                return
            
            data = response[0]
            price = data["current_price"]
            change = data["price_change_percentage_24h"]
            market_cap = data["market_cap"]
            volume = data["total_volume"]
            rank = data["market_cap_rank"]
            
            icon = "📈" if change >= 0 else "📉"
            change_str = f"+{change:.2f}%" if change >= 0 else f"{change:.2f}%"
            
            await ctx.send(f"""
```
💎 {data["name"]} ({data["symbol"].upper()})
━━━━━━━━━━━━━━━━━━━━━━
💰 Prezzo: ${price:,.2f}
{icon} 24h: {change_str}
📊 Market Cap: ${self.format_num(market_cap)}
📈 Volume: ${self.format_num(volume)}
🏆 Rank: #{rank}
```
""", delete_after=15)
        except Exception as e:
            await ctx.send(f"`❌ Errore: {str(e)}`", delete_after=5)

    def format_num(self, num):
        if num >= 1_000_000_000_000:
            return f"{num/1_000_000_000_000:.2f}T"
        elif num >= 1_000_000_000:
            return f"{num/1_000_000_000:.2f}B"
        elif num >= 1_000_000:
            return f"{num/1_000_000:.2f}M"
        elif num >= 1_000:
            return f"{num/1_000:.2f}K"
        return str(num)

async def setup(bot):
    await bot.add_cog(Crypto(bot))