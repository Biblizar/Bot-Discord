import asyncio
import discord
from discord.ext import commands


class Rules(commands.Cog):
    """Commandes sondage."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def regles(self,ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title='Les régles',
            description='1.Pas de spam\n2.Respecter les channels et leurs utilisation',
            color=discord.Colour.blurple()
        )
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Rules(bot))
