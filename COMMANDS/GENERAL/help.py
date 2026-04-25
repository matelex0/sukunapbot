from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, category=None):
        if category is None:
            embed_text = (
                "## 📘 HELP CATEGORIES\n\n"
                "> ### 🔹 GENERAL - `.help general`\n"
                "> *Basic commands and utilities*\n\n"
                "> ### 💰 CURRENCY - `.help currency`\n"
                "> *Currency conversion and crypto tools*\n\n"
                "> ### 🤡 FUN - `.help fun`\n"
                "> *Entertainment and fun commands*\n\n"
                "> ### 🔎 RESEARCH - `.help research`\n"
                "> *Search and information tools*\n\n"
                "**Use the commands above to get detailed information about each category.**\n"
                "*Tip: You can also use `.help <command>` to get specific command info*"
            )
            await ctx.send(embed_text)
        elif category.lower() == "general":
            general_commands = (
                "## 📘 GENERAL COMMANDS\n\n"
                "> ↪ **`.help`** - Shows all command categories\n"
                "> ↪ **`.ping`** - Bot latency (API + HTTP)\n"
                "> ↪ **`.info`** - System and bot info\n"
                "> ↪ **`.serverinfo`** - Server information\n"
                "> ↪ **`.servericon`** - Server icon\n"
                "> ↪ **`.avatar <user>`** - User avatar\n"
                "> ↪ **`.translate <from> <to> <text>`** - Translate text\n"
                "> ↪ **`.langs`** - Available languages\n"
                "> ↪ **`.setstatus <status>`** - Set status (online/idle/dnd/invisible)\n"
                "> ↪ **`.playing <text>`** - Playing status\n"
                "> ↪ **`.listening <text>`** - Listening status\n"
                "> ↪ **`.watching <text>`** - Watching status\n"
                "> ↪ **`.stream <url> <text>`** - Streaming status\n"
                "> ↪ **`.cactivity`** - Clear activity\n"
                "> ↪ **`.afk`** - AFK mode\n"
                "> ↪ **`.clear <n>`** - Delete n messages\n"
                "> ↪ **`.nsfw <category>`** - NSFW categories\n"
                "> ↪ **`.tos`** - Terms of Service\n"
            )
            await ctx.send(general_commands)

        elif category.lower() == "currency":
            currency_commands = (
                "## 💰 CURRENCY COMMANDS\n\n"
                "> ↪ **`.cryptoeur <coin>`** - Crypto price in EUR (price, 24h, market cap, rank)\n"
                "> ↪ **`.cryptousd <coin>`** - Crypto price in USD\n"
                "> ↪ **`.exchange <from> <to> <value>`** - Currency exchange\n"
                "> ↪ **`.ltcbal`** - Litecoin balance\n"
                "> ↪ **`.pp`** - PayPal link\n"
            )
            await ctx.send(currency_commands)

        elif category.lower() == "research":
            research_commands = (
                "## 🔎 RESEARCH COMMANDS\n\n"
                "> ↪ **`.yt <search>`** - Search on YouTube\n"
                "> ↪ **`.ipinfo <ip>`** - IP information\n"
                "> ↪ **`.checktoken <token>`** - Check Discord token\n"
                "> ↪ **`.web <search>`** - Google search\n"
            )
            await ctx.send(research_commands)
        
        elif category.lower() == "fun":
            fun_commands = (
                "## 🤡 FUN COMMANDS\n\n"
                "> ↪ **`.ascii <text>`** - Convert text to ASCII art\n"
                "> ↪ **`.iphonegift`** - Fake iPhone giveaway\n"
                "> ↪ **`.nitro`** - Fake Discord Nitro\n"
                "> ↪ **`.meme`** - Random meme\n"
                "> ↪ **`.joke`** - Random joke\n"
                "> ↪ **`.wl`** - Voice channel whitelist\n"
                "\n"
                "## 💎 GAMBLE SYSTEM\n\n"
                "> ↪ **`.bal`** - Check your coin balance\n"
                "> ↪ **`.daily`** - Claim daily reward (100-500 coins)\n"
                "> ↪ **`.bet <amount>`** - Bet your coins (50%+ chance to win!)\n"
                "\n*Start with 1000 coins!*"
            )
            await ctx.send(fun_commands)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))