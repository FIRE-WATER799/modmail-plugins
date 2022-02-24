import discord
from discord.ext import commands

class Test(Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test")