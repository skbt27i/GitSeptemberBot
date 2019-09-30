import discord
from discord.ext import commands


class SwiftleesCog(discord.Cog, name="Swiftlee's Cog"):

    @commands.command()
    async def swiftlee(self, ctx):
        await ctx.channel.send(f'Woah, you sent a message in {ctx.channel.name}!')
