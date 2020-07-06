import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        await ctx.message.delete()
        # retour en privée l'integralité des commandes disponible pour le bot
        guild_owner = ctx.message.guild.owner
        member = ctx.message.author
        if member == guild_owner:
            embedAdmin = discord.Embed(
                colour=discord.Colour.dark_red()
            )
            embedAdmin.set_author(name="les commandes discord de l'administrateur!")
            embedAdmin.add_field(name='$makeRules Regle1 | Regle2 | Regle3', value="Définie les regles du serveur")
            embedAdmin.add_field(name='$set Message | Emot1 : Role1 | Emot2 : Role2', value="Met en place un message pour que les utilisateurs s'attribuent des roles")
            embedAdmin.add_field(name='$roleModo', value='Permet au bot de savoir quel role est modérateur')
            await member.send(embed=embedAdmin)

        embed = discord.Embed(
            colour=discord.Colour.red()
        )
        embed.set_author(name='les commandes discord !')
        embed.add_field(name='$sondage Question | Prop1 | Prop2 | time=', value="Lance un sondage avec sa question, ses réponses et d'y ajouter un compte à rebours ")
        embed.add_field(name='$regles', value='Les regles du discord')
        embed.add_field(name='$modo', value='Affichage et ping les modérateurs du discord')
        embed.add_field(name='$bienvenue @user', value='Message de bienvenue')
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Help(bot))