import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        # retour en privée l'integralité des commandes disponible pour le bot
        embed = discord.Embed(
            colour=discord.Colour.red()
        )
        embed.set_author(name='les commandes discord !')
        embed.add_field(name='$set', value="définition d'un message de role")
        embed.add_field(name='$regles', value='Les regles du discord')
        embed.add_field(name='$modo', value='Affichage et ping des modérateurs du discord')
        embed.add_field(name='$bienvenue', value='Message de bienvenue')
        embed.set_footer(text='https://developpeurwebjunior.fr/')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))