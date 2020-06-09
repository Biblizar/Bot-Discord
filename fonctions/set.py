from discord.ext import commands
import json

class Setting(commands.Cog):
    """Commandes set."""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    @commands.has_role("Modo")
    async def set(self, ctx):
        await ctx.message.delete()
        message = await ctx.send("Ce message est le message de choix de role par défaut")
        role_message = message.id
        print(role_message)
        channel_role = message.channel.id
        print(channel_role)
        changed ={"channel": channel_role,"message": role_message}
        with open('config.json','w') as outfile:
            json.dump(changed, outfile)

def setup(bot):
    bot.add_cog(Setting(bot))

