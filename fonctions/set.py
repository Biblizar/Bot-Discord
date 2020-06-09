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
        set_message = await ctx.send("Vous pouvez choisir parmis les différentes réactions pour avoir accès aux salons correspondants")
        role_message = set_message.id
        print(role_message)
        channel_role = set_message.channel.id
        print(channel_role)
        changed ={"channel": channel_role,"message": role_message}
        with open('config.json','w') as outfile:
            json.dump(changed, outfile)

def setup(bot):
    bot.add_cog(Setting(bot))

