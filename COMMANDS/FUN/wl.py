from discord.ext import commands

class Whitelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.whitelist_enabled = False
        self.protected_channel = None
        self.allowed_users = set()
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def wl(self, ctx, channel: commands.VoiceChannelConverter = None, *members: commands.MemberConverter):
        if channel:
            self.protected_channel = channel.id
            self.whitelist_enabled = True
            if members:
                self.allowed_users = {str(member.id) for member in members}
                allowed_mentions = ", ".join(member.mention for member in members)
                await ctx.send(f"`📒 Whitelist protection is now enabled for channel {channel.name} with allowed users: {allowed_mentions}`", delete_after=5)
            else:
                await ctx.send(f"`📒 Whitelist protection is now enabled for channel {channel.name}`", delete_after=5)
        else:
            self.whitelist_enabled = not self.whitelist_enabled
            status = "enabled" if self.whitelist_enabled else "disabled"
            await ctx.send(f"`📒 Whitelist protection is now {status}`", delete_after=5)
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not self.whitelist_enabled or not self.protected_channel:
            return
            
        if after.channel and after.channel.id == self.protected_channel:
            if str(member.id) not in self.allowed_users and not member.voice:
                print(f"{member.name} ({member.id}) Tried to enter the vocal channel")
                try:
                    await member.move_to(None)
                except Exception as e:
                    print(f"Error disconnecting the user: {e}")
                    
        if before.channel and before.channel.id == self.protected_channel and (not after.channel or after.channel.id != self.protected_channel):
            if str(member.id) in self.allowed_users:
                try:
                    channel = self.bot.get_channel(self.protected_channel)
                    await member.move_to(channel)
                    print(f"{member.name} ({member.id}) Returned to the channel.")
                except Exception as e:
                    print(f"Error during the move of the user: {e}")

async def setup(bot):
    await bot.add_cog(Whitelist(bot))