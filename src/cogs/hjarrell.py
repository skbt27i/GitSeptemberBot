import os

import discord
from discord.ext import commands

class hjarrell(commands.Cog, name='HJarrell'):
    """Hunter Jarrell's example cog"""

    ADMIN_ROLE_ID = 628077277107847198

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(hidden=True)
    @commands.has_role(ADMIN_ROLE_ID)
    async def reload(self, ctx):
        """Unloads and then loads an extension"""
        for cog in os.listdir('src/cogs'):
            if cog.endswith('.py'):
                try:
                    self.bot.reload_extension('cogs.' + cog[:-3])
                except commands.ExtensionNotLoaded:
                    self.bot.load_extension('cogs.' + cog[:-3])
                except Exception:
                    await ctx.send(f'Error loading {cog}')
        await ctx.send("Reloaded.")


def setup(bot):
    bot.add_cog(hjarrell(bot))
