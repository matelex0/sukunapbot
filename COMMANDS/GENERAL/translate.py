from discord.ext import commands
from googletrans import Translator, LANGUAGES

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @commands.command()
    async def translate(self, ctx, from_lang, to_lang, *, text):
        try:
            if from_lang.lower() not in LANGUAGES and from_lang.lower() != 'auto':
                await ctx.send("`❌ Invalid source language code`", delete_after=5)
                return
            if to_lang.lower() not in LANGUAGES:
                await ctx.send("`❌ Invalid target language code`", delete_after=5)
                return

            translated = await self.translator.translate(text, src=from_lang.lower(), dest=to_lang.lower())
            await ctx.send(f"`🌐 Translation ({from_lang} ➜ {to_lang}):`\n\n> **{translated.text}**")
        except Exception as e:
            await ctx.send(f"`❌ Error: {str(e)}`", delete_after=5)

async def setup(bot):
    await bot.add_cog(Translate(bot))