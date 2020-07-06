#on importe le module discord
import asyncio
import json
import discord
from discord.utils import get
from discord.ext import commands

#on charge le fichier json contenant le token de l'application
with open("token.json","r") as conffile:
    config = json.load(conffile)


#on crée une instance du Bot et on applique un prefix
bot = commands.Bot(command_prefix='$', description="Voici les différentes commandes utilisables a l'heure actuelle")
bot.remove_command('help')


startup_extensions = ["fonctions.help","fonctions.sondage", "fonctions.set", "fonctions.welcome", "fonctions.rules",
                       "fonctions.Modo","fonctions.update"]

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
    await bot.change_presence(status=discord.Status.online)


@bot.event
async def on_raw_reaction_add(payload):
    with open("config.json", "r") as outfiler:
        config = json.load(outfiler)
    emoji = payload.emoji
    canal = payload.channel_id
    id_server = payload.guild_id
    serv_param = config[str(id_server)]
    message = payload.message_id
    member = bot.get_guild(id_server).get_member(payload.user_id)
    print(f"L'id du channel:{serv_param['channel']} et l'id du message: { serv_param['message'] }")
    print(message, canal)
    for emot in serv_param["emot_role"]:
        if canal == serv_param["channel"] and message == serv_param['message'] and str(emoji) == str(emot):
            new_role = get(bot.get_guild(payload.guild_id).roles, name=f"{serv_param['emot_role'][emot]}")
            await member.add_roles(new_role)

@bot.event
async def on_raw_reaction_remove(payload):
    with open("config.json", "r") as outfiler:
        config = json.load(outfiler)
    emoji = payload.emoji
    canal = payload.channel_id
    message = payload.message_id
    id_server = payload.guild_id
    serv_param = config[str(id_server)]
    member = bot.get_guild(id_server).get_member(payload.user_id)
    for emot in serv_param["emot_role"]:
        if canal == serv_param["channel"] and message == serv_param['message'] and str(emoji) == str(emot):
            new_role = get(bot.get_guild(payload.guild_id).roles, name=f"{serv_param['emot_role'][emot]}")
            await member.remove_roles(new_role)

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