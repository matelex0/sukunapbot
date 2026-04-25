from discord.ext import commands
import random
import json
import os

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data_file = "gamble_data.json"
        self.data = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                return json.load(f)
        return {"users": {}}
    
    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=4)
    
    def get_balance(self, user_id):
        return self.data["users"].get(str(user_id), 1000)
    
    def set_balance(self, user_id, amount):
        self.data["users"][str(user_id)] = amount
        self.save_data()
    
    @commands.command(aliases=["bal"])
    async def balance(self, ctx):
        await ctx.message.delete()
        balance = self.get_balance(ctx.author.id)
        await ctx.send(f"`💰 Balance: {balance} coins`", delete_after=10)
    
    @commands.command()
    async def daily(self, ctx):
        await ctx.message.delete()
        user_id = str(ctx.author.id)
        if "last_daily" not in self.data:
            self.data["last_daily"] = {}
        
        import time
        current_time = time.time()
        last_daily = self.data["last_daily"].get(user_id, 0)
        
        if current_time - last_daily < 86400:
            remaining = int(86400 - (current_time - last_daily))
            hours = remaining // 3600
            minutes = (remaining % 3600) // 60
            await ctx.send(f"`⏰ Daily already claimed! Come back in {hours}h {minutes}m`", delete_after=10)
            return
        
        self.data["last_daily"][user_id] = current_time
        reward = random.randint(100, 500)
        self.set_balance(ctx.author.id, self.get_balance(ctx.author.id) + reward)
        self.save_data()
        await ctx.send(f"`🎁 Daily reward: +{reward} coins!`", delete_after=10)
    
    @commands.command()
    async def bet(self, ctx, amount: int):
        await ctx.message.delete()
        if amount <= 0:
            await ctx.send(f"`❌ Amount must be positive!`", delete_after=10)
            return
        
        current = self.get_balance(ctx.author.id)
        if amount > current:
            await ctx.send(f"`❌ Not enough coins! Balance: {current}`", delete_after=10)
            return
        
        roll = random.randint(1, 100)
        if roll <= 50:
            loss = amount
            new_balance = current - loss
            self.set_balance(ctx.author.id, new_balance)
            result = f"❌ You lost! Rolled: {roll}"
        else:
            if roll >= 90:
                multiplier = 3
                gain = amount * multiplier
                result = f"🎉 JACKPOT! x3! Rolled: {roll}"
            elif roll >= 70:
                multiplier = 2
                gain = amount * multiplier
                result = f"🎉 Big win! x2! Rolled: {roll}"
            else:
                multiplier = 1.5
                gain = int(amount * multiplier)
                result = f"🎉 You won! x1.5! Rolled: {roll}"
            
            new_balance = current + gain - amount
            self.set_balance(ctx.author.id, new_balance)
        
        await ctx.send(f"{result} | Balance: {new_balance}", delete_after=15)

async def setup(bot):
    await bot.add_cog(Gamble(bot))