from discord.ext import commands
import aiohttp
import asyncio

class LitecoinCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = {}
        with open("CONFIG.txt") as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    self.config[k] = v.strip('"').strip("'").strip()

    @commands.command()
    async def ltcbal(self, ctx):
        try:
            address = self.config.get("LTC_ADDRESS", "")
            if not address:
                await ctx.send("`❌ LTC address not configured in CONFIG.txt`", delete_after=5)
                return

            async with aiohttp.ClientSession() as session:
                tasks = [
                    session.get(f"https://api.blockcypher.com/v1/ltc/main/addrs/{address}/balance"),
                    session.get("https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd,eur"),
                    session.get(f"https://api.blockcypher.com/v1/ltc/main/addrs/{address}/full?limit=3")
                ]
                responses = await asyncio.gather(*tasks)
                
                balance_response, price_response, tx_response = responses
                
                if balance_response.status != 200:
                    await ctx.send("`❌ Failed to fetch balance`", delete_after=5)
                    return
                data = await balance_response.json()
                balance = data.get("balance", 0) / 100000000

                if price_response.status != 200:
                    await ctx.send("`❌ Failed to fetch price data`", delete_after=5)
                    return
                price_data = await price_response.json()
                ltc_usd = price_data["litecoin"]["usd"]
                ltc_eur = price_data["litecoin"]["eur"]
                usd_value = balance * ltc_usd
                eur_value = balance * ltc_eur

                if tx_response.status != 200:
                    await ctx.send("`❌ Failed to fetch transactions`", delete_after=5)
                    return
                tx_data = await tx_response.json()
                    
                response = [
                    "",
                    f"```📋 Address: {address}",
                    f"💰 Litecoin Balance: {balance:.8f} LTC",
                    f"USD Value: ${usd_value:.2f}",
                    f"EUR Value: €{eur_value:.2f}",
                    "\nRecent Transactions:```"
                ]
                
                for tx in tx_data.get("txs", []):
                    received = sum(output["value"] for output in tx["outputs"] if address in output.get("addresses", [])) / 100000000
                    sent = sum(input["output_value"] for input in tx["inputs"] if address in input.get("addresses", [])) / 100000000
                    if received > 0:
                        response.append(f"`➡️ Received: {received:.8f} LTC`")
                    if sent > 0:
                        response.append(f"`⬅️ Sent: {sent:.8f} LTC`")
                
                response.append("")
                await ctx.send("\n".join(response))
        except Exception as e:
            await ctx.send(f"`❌ Error: {str(e)}`", delete_after=5)

async def setup(bot):
    await bot.add_cog(LitecoinCommands(bot))