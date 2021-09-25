import discord
import asyncio
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation cog is active.')

    @commands.command(name='unban')
    @commands.guild_only()
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned user.') 

    @commands.command(name='clear')
    async def clear(self, ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Deleted {amount} messages.')
        await asyncio
        await ctx.channel.purge(1)

    @commands.command(name='kick')
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} was kicked from the server for, Reason: {reason}')


    @commands.command(name='ban')
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} was banned from the server for, Reason: {reason}')

      


def setup(client):
    client.add_cog(Moderation(client))
