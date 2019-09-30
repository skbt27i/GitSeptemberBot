import discord
from discord.ext import commands

class Ping(commands.Cog, name='Ping'):
    """Classic Ping->Pong example"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        """Unloads and then loads an extension"""
        await ctx.send("Pong test")


def setup(bot):
    bot.add_cog(Ping(bot))
