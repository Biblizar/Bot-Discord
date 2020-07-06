from discord.ext import commands


class Update(commands.Cog):
    """Commandes sondage."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def update(self, ctx, msg):
        await ctx.message.delete()
        guildList = self.bot.guilds
        print(guildList)
        for guild in guildList:
            owner = guild.owner
            print(owner)
            await owner.send(f"Bonjour {owner.mention}\n{msg}\n Merci de ton attention.")





def setup(bot):
    bot.add_cog(Update(bot))