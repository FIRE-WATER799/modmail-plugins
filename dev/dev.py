import discord
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands


Cog = getattr(commands, "Cog", object)

class Dev(Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test")
    
    @commands.command()
    async def review(self, ctx, *, rating=None):
        """Provide your rating of my services on a scale of 10"""
        if rating == None:
            await ctx.send("You did not provide a rating")
        else:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/985380251628601374/RwjOcAbSUDLGwKciOLuS9kw7J8ct4Uba-zARm-_IbEY0NZZvBKNRZzi7TGhIclaIAk4F', adapter=RequestsWebhookAdapter())
            rate = discord.Embed(title="Rating")
            rate.add_field(name="Name", value=ctx.author.name)
            rate.add_field(name="Rating", value = str(rating) + "This is the users rating")
            webhook.send(embed=rate)

def setup(bot):
    bot.add_cog(Dev(bot))