import discord
from discord.ext import commands

# TODO Change Ping and name to your cog name
class Ping(commands.Cog, name='Ping'):
    """Classic Ping->Pong example"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        """Unloads and then loads an extension"""
        # Send when the user says !ping
        await ctx.send("Pong")
	

def setup(bot):
    # Tell the bot about our cog
    # TODO Change Ping to your class name
    bot.add_cog(Ping(bot))

