import discord
from discord.ext import commands

Cog = getattr(commands, "Cog", object)

class Test(Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test")
    
    @commands.command()
    async def say(self, ctx, *, arg=None):
        if arg == None:
            embed = discord.Embed(
                color=0xFF0000
                )  
            embed.add_field(name='Error', value="Please specify what you want me to say.", inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                color=0x2ECC71
                )  
            embed.add_field(name=f'{ctx.message.author.name}', value=f"{arg}", inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Test(bot))