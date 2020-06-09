#on importe le module discord
import asyncio
import json
import discord
from fonctions import set
from discord.utils import get
from discord.ext import commands


#on charge le fichier json contenant le token de l'application
with open("token.json","r") as conffile:
    config = json.load(conffile)

#on crée une instance du Bot et on applique un prefix
bot = commands.Bot(command_prefix='$', description="Voici les différentes commandes utilisables a l'heure actuelle")
bot.remove_command('help')


startup_extensions = ["fonctions.help","fonctions.sondage", "fonctions.set", "fonctions.welcome", "fonctions.rules"]

async def my_background_task(self):
    with open("config.json", "r") as outfiler:
        serv_param = json.load(outfiler)

    await self.wait_until_ready()
    counter = 0
    channel = self.get_channel(serv_param['channel'])  # channel ID goes here
    while not self.is_closed():
        counter += 1
        await channel.send(counter)
        await asyncio.sleep(60)  # task runs every 60 seconds




@bot.event
async def on_ready():
    print('en ligne en tant que')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Game(name="cherche un job")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_raw_reaction_add(payload):
    with open("config.json", "r") as outfiler:
        serv_param = json.load(outfiler)
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    python_role = get(bot.get_guild(payload.guild_id).roles, name="Python")
    php_role = get(bot.get_guild(payload.guild_id).roles, name="Php")
    javascript_role = get(bot.get_guild(payload.guild_id).roles, name="Javascript")
    member = bot.get_guild(payload.guild_id).get_member(payload.user_id)
    print(f"L'id du channel:{serv_param['channel']} et l'id du message: { serv_param['message'] }")
    print(message, canal)
    if canal == serv_param['channel'] and message == serv_param['message']:
        if emoji == "python":
            await member.add_roles(python_role)
        elif emoji == "php":
            await member.add_roles(php_role)
        elif emoji == "javascript":
            await member.add_roles(javascript_role)

@bot.event
async def on_raw_reaction_remove(payload):
    with open("config.json", "r") as outfiler:
        serv_param = json.load(outfiler)
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    python_role = get(bot.get_guild(payload.guild_id).roles, name="Python")
    php_role = get(bot.get_guild(payload.guild_id).roles, name="Php")
    javascript_role = get(bot.get_guild(payload.guild_id).roles, name="Javascript")

    member = bot.get_guild(payload.guild_id).get_member(payload.user_id)
    if canal == serv_param['channel'] and message == serv_param['message']:
        if emoji == "python":
            await member.remove_roles(python_role)
        elif emoji == "php":
            await member.remove_roles(php_role)
        elif emoji == "javascript":
            await member.remove_roles(javascript_role)


@bot.command()
async def modo(ctx):
    modo_role = get(bot.get_guild("GUILD ID HERE").roles, name="Modo").mention
    embed = discord.Embed(
        title='Les Modérateurs du Discord',
        description = f'Si tu as un problème n\'hésite pas à contacter un des {modo_role} ci dessous',
        color=discord.Colour.red()
    )
    embed.set_author(name='BibliBot')
    embed.add_field(name='Admin du discord', value='@NicolasRz', inline=True)
    embed.add_field(name='Modérateur ',value='@Djohn', inline=False)
    embed.add_field(name='  Modérateur ',value='@Mikaël', inline=False)

    await ctx.send(embed=embed)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

print("Lancement du bot")
#donner le jeton pour qu'il se connecte
bot.run(config["token"])