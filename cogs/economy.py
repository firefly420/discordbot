import discord
import random
import json
import os


from discord.ext import commands

class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Economy cog is active.')

    async def open_account(self, user):

        users = await get_bank_data()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 100
            users[str(user.id)]["bank"] = 100

        with open("bank.json","w") as f:
            json.dump(users,f)
        return True

    async def get_bank_data(self):
        with open("bank.json","r") as f:
            users = json.load(f)
        return users


    @commands.command(name='bal')
    async def bal(self, ctx):
        user = ctx.author
        await open_account(ctx.author)
        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.red())
        em.add_field(name = "Wallet balance",value = wallet_amt)
        em.add_field(name = "Bank balance",value = bank_amt)
        await ctx.send(embed = em)

    @commands.command(name='work')
    async def work(self, ctx):
        await open_account(ctx.author)
        
        users = await get_bank_data()

        user = ctx.author

        earnings = random.randrange(101)

        await ctx.send(f"You scubbed toilets and got ${earnings}")


        users[str(user.id)]["wallet"] += earnings

        with open("bank.json","w") as f:
            json.dump(users,f)
    
def setup(client):
    client.add_cog(Economy(client))
