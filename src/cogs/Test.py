import discord
from discord.ext import commands

# TODO Change Ping and name to your cog name
class Test(commands.Cog, name='Test'):
    """Classic Ping->Pong example"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        """Unloads and then loads an extension"""
        await ctx.send("Test Successful")
	

	

def setup(bot):
    # Tell the bot about our cog
    # TODO Change Ping to your class name
	bot.add_cog(Test(bot))

