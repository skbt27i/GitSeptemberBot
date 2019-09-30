import discord
    from discord.ext import commands
class Ben(commands.Cog, name=’Ben’'):
    def __init__(self, bot, db):
        self.bot = bot
@commands.command()
    async def yourCommand(self, ctx, a=0, b=0):
        """Sends a message to the channel you executed your command on."""
        await ctx.channel.send(f'The sum of {a} + {b} = {a+b}')
def setup(bot):
    bot.add_cog(MessageSender(bot))
