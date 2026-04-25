from discord.ext import commands
import aiohttp

LANGUAGES = {
    "en": "English", "it": "Italian", "es": "Spanish", "fr": "French",
    "de": "German", "pt": "Portuguese", "ru": "Russian", "ja": "Japanese",
    "ko": "Korean", "zh": "Chinese", "ar": "Arabic", "hi": "Hindi",
    "nl": "Dutch", "pl": "Polish", "tr": "Turkish", "vi": "Vietnamese"
}

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = None

    async def cog_load(self):
        self.session = aiohttp.ClientSession()
    
    async def cog_unload(self):
        if self.session:
            await self.session.close()

    @commands.command()
    async def translate(self, ctx, from_lang, to_lang, *, text):
        if from_lang.lower() not in LANGUAGES and from_lang.lower() != "auto":
            await ctx.send(f"`❌ Lingua sorgente non valida. Disponibili: {', '.join(LANGUAGES.keys())}`", delete_after=5)
            return
        if to_lang.lower() not in LANGUAGES:
            await ctx.send(f"`❌ Lingua destinazione non valida. Disponibili: {', '.join(LANGUAGES.keys())}`", delete_after=5)
            return

        try:
            url = "https://api.mymemory.translated.net/get"
            params = {"q": text, "langpair": f"{from_lang}|{to_lang}"}
            async with self.session.get(url, params=params, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    if data["responseStatus"] == 200:
                        result = data["responseData"]["translatedText"]
                        await ctx.send(f"`🌐 {LANGUAGES.get(from_lang, from_lang)} → {LANGUAGES.get(to_lang, to_lang)}:`\n\n> **{result}**", delete_after=15)
                    else:
                        await ctx.send(f"`❌ Errore traduzione: {data.get('responseDetails', 'Unknown')}`", delete_after=5)
                else:
                    await ctx.send(f"`❌ Errore API: {resp.status}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"`❌ Errore: {str(e)}`", delete_after=5)

    @commands.command()
    async def langs(self, ctx):
        lang_list = ", ".join(f"`{k}`" for k, v in LANGUAGES.items())
        await ctx.send(f"**🌐 Lingue disponibili:**\n{lang_list}", delete_after=15)

async def setup(bot):
    await bot.add_cog(Translate(bot))