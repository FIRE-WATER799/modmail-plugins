import discord
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands


Cog = getattr(commands, "Cog", object)

class Dev(Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
    
    @commands.command()
    async def order(self, ctx, server = "Not Provided", *, reason = "Not provided"):
        """To order a modmail bot do {prefix}order [server invite link] [reason you want a bot]"""
        webhook = Webhook.from_url('https://discord.com/api/webhooks/985380251628601374/RwjOcAbSUDLGwKciOLuS9kw7J8ct4Uba-zARm-_IbEY0NZZvBKNRZzi7TGhIclaIAk4F', adapter=RequestsWebhookAdapter())
        order = discord.Embed(title="Order")
        order.add_field(name="Server Bot", value=self.bot.user.name)
        order.add_field(name="Name", value=str(ctx.author.name)+"#"+str(ctx.author.discriminator))
        order.add_field(name="User ID", value=ctx.author.id)
        order.add_field(name="Server", value = server)
        order.add_field(name="Reason", value=reason)
        webhook.send(embed=order)
        await ctx.send("Order sent, this is your order", embed=order)
    
    @commands.command()
    async def review(self, ctx, rating=None, *, reason="None provided"):
        """Provide your rating of my services on a scale of 10 and then a reason you gave me this rating."""
        if rating == None:
            await ctx.send("You did not provide a rating")
        else:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/985380251628601374/RwjOcAbSUDLGwKciOLuS9kw7J8ct4Uba-zARm-_IbEY0NZZvBKNRZzi7TGhIclaIAk4F', adapter=RequestsWebhookAdapter())
            rate = discord.Embed(title="Rating")
            rate.add_field(name="Server Bot", value=self.bot.user.name)
            rate.add_field(name="Name", value=str(ctx.author.name)+"#"+str(ctx.author.discriminator))
            rate.add_field(name="User ID", value=ctx.author.id)
            rate.add_field(name="Rating", value = "The user provided a rating of " + str(rating) + "/10")
            rate.add_field(name="Reason", value=reason)
            webhook.send(embed=rate)
            await ctx.send("Reveiw sent, this is your review", embed=rate)

def setup(bot):
    bot.add_cog(Dev(bot))