import discord
from discord.ext import commands
from discord.utils import get
import json

class Modo(commands.Cog):
    """Commandes set."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def roleModo(self, ctx, msg="help"):
        id_server = ctx.message.channel.guild.id
        await ctx.message.delete()
        config_file = open("config.json", "r")
        json_object = json.load(config_file)
        config_file.close()
        if msg != "help":
            modo_role = msg
            if get(ctx.guild.roles, name=f"{modo_role}"):
                await ctx.send('Le role existe et sera défini comme role modérateur')
                if str(id_server) in json_object:
                    json_object[str(id_server)]["modo_role"] = modo_role
                else:
                    json_object[str(id_server)] = {}
                    json_object[str(id_server)]["modo_role"] = modo_role
                config_file =  open('config.json','w')
                json.dump(json_object, config_file, indent=2)
                config_file.close()
            else:
                await ctx.send("Ce role n'existe pas")

    @roleModo.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send("Vous n'avez pas le droit d'utiliser cette commande")

    @commands.command()
    async def modo(self, ctx):
        config_file = open("config.json", "r")
        json_object = json.load(config_file)
        config_file.close()
        id_server = ctx.message.channel.guild.id
        guild_owner = ctx.message.guild.owner
        modo_role = get(self.bot.get_guild(id_server).roles, name=f"{json_object[str(id_server)]['modo_role']}")
        embed = discord.Embed(
            title='Les Modérateurs du Discord',
            description=f'Si tu as un problème n\'hésite pas à contacter un des {modo_role.mention} ci dessous',
            color=modo_role.color
        )
        embed.set_author(name='BibliBot')
        embed.add_field(name='Admin du discord', value=f'{guild_owner.mention}', inline=True)
        for member in modo_role.members:
            if member != guild_owner:
                embed.add_field(name=f'{modo_role}', value=f'{member.mention}', inline=True)
        await ctx.message.delete()

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Modo(bot))