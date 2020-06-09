import asyncio
import discord
from discord.ext import commands


class Welcome(commands.Cog):
    """Commandes bienvenue."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bienvenue(self, ctx, new_member: discord.Member):
        pseudo = new_member.mention
        await ctx.send(
            f"Bienvenue {pseudo}, si tu as besoin d'aide n'hésite pas à poser des questions ou utiliser les commandes $regles et $help")

def setup(bot):
    bot.add_cog(Welcome(bot))