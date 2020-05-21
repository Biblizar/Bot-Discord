#on importe le module discord
import discord
from discord.utils import get
from discord.ext import commands

#on crée une instance du Bot
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("Bot pret")

@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    guild = payload.guild_id
    python_role = get(bot.get_guild(payload.guild_id).roles, name="Python")
    php_role = get(bot.get_guild(payload.guild_id).roles, name="Php")
    javascript_role = get(bot.get_guild(payload.guild_id).roles, name="Javascript")
    member = bot.get_guild(payload.guild_id).get_member(payload.user_id)
    print(message, canal)
    if canal == "id du channel" and message == "id du message":
        if emoji == "python":
            await member.add_roles(python_role)
        elif emoji == "php":
            await member.add_roles(php_role)
        elif emoji == "javascript":
            await member.add_roles(javascript_role)

@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    python_role = get(bot.get_guild(payload.guild_id).roles, name="Python")
    php_role = get(bot.get_guild(payload.guild_id).roles, name="Php")
    javascript_role = get(bot.get_guild(payload.guild_id).roles, name="Javascript")

    member = bot.get_guild(payload.guild_id).get_member(payload.user_id)
    if canal == "id du channel" and message == "id du message":
        if emoji == "python":
            await member.remove_roles(python_role)
        elif emoji == "php":
            await member.remove_roles(php_role)
        elif emoji == "javascript":
            await member.remove_roles(javascript_role)

@bot.command()
async def regles(ctx):
    embed = discord.Embed(
        title='Les régles',
        description = '1.Pas de spam\n2.Respecter les channels et leurs utilisation',
        color=discord.Colour.blurple()
    )
    await ctx.send(embed=embed)

@bot.command()
async def modo(ctx):
    modo_role = get(bot.get_guild("ID du serveur).roles, name="Modo").mention
    embed = discord.Embed(
        title='Les Modérateurs du Discord',
        description = f'Si tu as un problème n\'hésite pas à contacter un des {modo_role} si dessous',
        color=discord.Colour.red()
    )
    embed.set_author(name='BibliBot')
    embed.add_field(name='Admin', value='@NicolasRz', inline=True)
    embed.add_field(name='Modérateur1',value='@Djohn', inline=False)
    embed.add_field(name='Modérateur2',value='@Mikaël', inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def bienvenue(ctx, new_member: discord.Member):
    pseudo = new_member.mention
    await ctx.send(f"Bienvenue {pseudo} la commande $regles et $help sont la pour toi")

#donner le jeton pour qu'il se connecte
jeton = "jeton du bot"

print("Lancement du bot")

bot.run(jeton)
