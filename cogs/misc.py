import discord
import random

from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Misc cog is active.')

    @commands.command(name ='ehtball', aliases=['8ball', '8b'])
    async def ehtball(self, ctx, *, question):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You know it's true.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(name='roulette')
    async def roulette(self, ctx):
        roulettepossibilities = ["You load in a bullet and spin the cylinder, ... **click** You survived, this time...",
                                 "You load in a bullet and spin the cylinder, ... **BANG** Oh dear, you died.",
                                 "You spin the cylinder and pray, ... **click** Not today satan!",
                                 "You spin the cylinder and pray, ... **BANG** Guess it wasn't your lucky day.",]

        await ctx.send(random.choice(roulettepossibilities))

    @commands.command(name='penismeasure', aliases=['pm','pid'])
    async def penismeasure(self, ctx):

        await ctx.send(f'{ctx.message.author.mention} Your penis is {random.randint(0,12)} inches long.')


def setup(client):
    client.add_cog(Misc(client))
