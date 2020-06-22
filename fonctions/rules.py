import asyncio
import discord
from discord.ext import commands
import json


class Rules(commands.Cog):
    """Commandes sondage."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def makeRules(self, ctx, *, msg):
        id_server = ctx.message.channel.guild.id
        with open("config.json", "r") as f:
            config = json.load(f)
        await ctx.message.delete()
        rules = msg.split(" | ")
        if str(id_server) in config:
            config[str(id_server)]["regles"] = []
            config[str(id_server)]["regles"] = rules
            with open("config.json", "w") as f:
                json.dump(config, f, indent=2)
        else:
            config[str(id_server)] = {}
            config[str(id_server)]["regles"] = []
            config[str(id_server)]["regles"] = rules
            with open("config.json", "w") as f:
                json.dump(config, f, indent=2)
        i = 0
        definedRules = ""
        for rule in rules:
            i += 1
            print(i)
            definedRules = f"{definedRules} \n {i}.{rule}"
        embed = discord.Embed(
            title='Discord Rules',
            description=definedRules,
            color=discord.Colour.dark_red()
        )
        embed.set_author(name='BibliBot')
        await ctx.send(embed=embed)

    @commands.command()
    async def regles(self, ctx):
        id_server = ctx.message.channel.guild.id
        with open("config.json", "r") as f:
            config = json.load(f)
        await ctx.message.delete()
        if str(id_server) in config:
            rules = config[str(id_server)]["regles"]
            i = 0
            definedRules = ""
            for rule in rules:
                i += 1
                print(i)
                definedRules = f"{definedRules} \n {i}.{rule}"
            embed = discord.Embed(
                title='Discord Rules',
                description=definedRules,
                color=discord.Colour.dark_red()
            )
            embed.set_author(name='BibliBot')
            await ctx.send(embed=embed)
        else:
            await ctx.send("Ce discord ne possède pas de réglement")

def setup(bot):
    bot.add_cog(Rules(bot))
