import discord
from discord.ext import commands

from config import BOT_TOKEN

INVITE_URL = bot_url = 'https://discordapp.com/api/oauth2/authorize?client_id={0}&scope=bot&permissions=0'

def main():
    bot = commands.Bot(command_prefix='!', description='GitSeptember Teaching Bot')

    @bot.event
    async def on_ready():
        """Print the bots information on connect"""
        print('Logged in as "{name}" with id {id}'.format(name=bot.user.name,id=bot.user.id))
        print('Invite URL: {iurl}'.format(iurl=INVITE_URL.format(bot.user.id)))
        print('-----')

    # TODO Change hjarrell to your cog name
    bot.load_extension('cogs.hjarrell')
    bot.load_extension('cogs.Ping')
    bot.load_extension('cogs.Test')
    bot.run(BOT_TOKEN)

if __name__ == "__main__":
    main()
