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
                "> ↪ **`.afk`** - You go in afk mode\n"
                "> ↪ **`.clear <value>`** - Purge 1 or more of your texts\n"
                "> ↪ **`.spam <text>`** - Spam what text do you want\n"
                "> ↪ **`.spamreact <emoji>`** - Spam what react do you want\n"
                "> ↪ **`.avatar <user>`** - Get a user icon/avatar.\n"
                "> ↪ **`.info`** - Get info about selfbot creator and much more.\n"
                "> ↪ **`.nsfw <category>`** - If you tipe only .nsfw, it will apear all categories.\n"
                "> ↪ **`.ping`** - Pong\n"
                "> ↪ **`.serverinfo`** - Will pop up all info about the server\n"
                "> ↪ **`.servericon`** - Will send the server icon\n"
                "> ↪ **`.playing <text>`** - Custom activity\n"
                "> ↪ **`.stream <text>`** - Custom activity\n"
                "> ↪ **`.cactivity <activity>`** - Clear Custom activity\n"
                "> ↪ **`.setstatus <status dnd, invisible, idle, online>`** - Set status\n"
                "> ↪ **`.translate <from-lang> <to-lang> <text>`** - Translate, use language format like [en, it] ecc...\n"
                "> ↪ **`.autoreply <on|off>`** - AutoReply [MAINTENANCE]\n\n"
            )
            await ctx.send(general_commands)

        elif category.lower() == "currency":
            currency_commands = (
                "## 💰 CURRENCY COMMANDS\n\n"
                "> ↪ **`.cryptoeur <crypto>`** - Sends crypto value in eur\n"
                "> ↪ **`.cryptousd <crypto>`** - Sends crypto value in usd\n"
                "> ↪ **`.exchange <from-currency> <to-currency> <value>`** - Exchange of currency\n"
                "> ↪ **`.ltcbal`** - Show's your litecoin balance\n"
                "> ↪ **`.pp`** - Paypal personal link\n\n"
            )
            await ctx.send(currency_commands)

        elif category.lower() == "research":
            research_commands = (
                "## 🔎 RESEARCH COMMANDS\n\n"
                "> ↪ **`.yt <search>`** - Search anything you want on youtube\n"
                "> ↪ **`.ipinfo <ip>`** - Ip info\n"
                "> ↪ **`.checktoken <token>`** - Check Discord Token\n"
                "> ↪ **`.web <search>`** - Search anything you want on the web\n\n"
            )
            await ctx.send(research_commands)
        
        elif category.lower() == "fun":
            fun_commands = (
                "## 🤡 FUN COMMANDS\n\n"
                "> ↪ **`.ascii <text>`** - Transform your text in ascii\n"
                "> ↪ **`.iphonegift`** - Fake Iphone giveaway\n"
                "> ↪ **`.nitro`** - Fake Nitro\n"
                "> ↪ **`.meme`** - Sends a blank meme\n"
                "> ↪ **`.joke`** - Sends a joke of the day\n"
                "> ↪ **`.wl`** - Whitelist for you and your friends in a vocal channel\n"
                "> ↪ **`.web <search>`** - Search anything you want on the web\n\n"
            )
            await ctx.send(fun_commands)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))