from discord.ext import commands
import requests

class Crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cryptoeur(self, ctx, coin: str):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=eur"
        response = requests.get(url).json()
        if coin not in response:
            await ctx.send("`❌ Crypto not found!`", delete_after=5)
            return
            
        price = response[coin]["eur"]
        
        await ctx.send(f"> **💶 {coin.capitalize()} is worth {price} EUR**", delete_after=5)

    @commands.command()
    async def cryptousd(self, ctx, coin: str):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url).json()
        if coin not in response:
            await ctx.send("`❌ Crypto not found!`", delete_after=5)
            return
            
        price = response[coin]["usd"]
        
        await ctx.send(f"> **💶 {coin.capitalize()} is worth {price} USD**", delete_after=5)

async def setup(bot):
    await bot.add_cog(Crypto(bot))