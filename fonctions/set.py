from discord.ext import commands
import json

class Setting(commands.Cog):
    """Commandes set."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def set(self, ctx, *, msg):
        splitting_message = msg.split(" | ")
        id_server = ctx.message.channel.guild.id
        with open("config.json", "r") as f:
            config = json.load(f)
        await ctx.message.delete()
        set_message = await ctx.send(splitting_message[0])

        if str(id_server) in config:
            config[str(id_server)]["message"] = set_message.id
            config[str(id_server)]["channel"] = set_message.channel.id
            with open("config.json", "w") as f:
                json.dump(config, f, indent=2)
        else:
            config[str(id_server)] = {}
            config[str(id_server)]["message"] = set_message.id
            config[str(id_server)]["channel"] = set_message.channel.id
            with open("config.json", "w") as f:
                json.dump(config, f, indent=2)


        config[str(id_server)]["emot_role"] = {}
        for splitted_message in splitting_message[1:]:
            emot_role = splitted_message.split(" : ")
            config[str(id_server)]["emot_role"][emot_role[0]] = emot_role[1]
            await set_message.add_reaction(emot_role[0])
        with open("config.json", "w") as f:
            json.dump(config, f, indent=2)

def setup(bot):
    bot.add_cog(Setting(bot))
