"""
To add:
Cogs
Database for Logs
Artifact and CCU related commands
CCU Stock API
Chess API
Tik Tac Toe
Dictionary API for word definitions ^query
discord/markov api
"""


import os
from twitchio.ext import commands
import asyncio

#requirements for cogs
import chess
import random

print("forsenL")

class forsenL(commands.Bot):
    def __init__(self):
        super().__init__(client_secret="[insert clien_secret]", token="[insert token]", prefix="^", initial_channels=["catsh"])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        offline_only = ["minusinsanity"]
        if message.echo:
            return
        elif offline_only.count(message.channel.name) == -1:
            return
        elif message.content == ("forsen"):
            await message.channel.send("forsen")
        elif message.content == ("sigma"):
            await message.channel.send("sigma")
        tim = str(message.timestamp.year) + ":" + str(message.timestamp.month) + ":" + str(message.timestamp.day) + ":" + str(message.timestamp.hour) + ":" + str(message.timestamp.minute)
        mess = tim + " | " + message.author.display_name + ": " + message.content + " | " + message.channel.name
        print(mess)
        with open("logs.txt", "a", encoding= "utf-8") as forse:
            forse.write("\n"+ mess)
        await self.handle_commands(message)
    
    @commands.command()
    async def forsen(self, ctx: commands.Context, fors = None):
        if fors == None:
            await ctx.send("forsen")
        else:
            await ctx.send(f'forsen "{fors}"')

    @commands.command(aliases= ["poro", "commands"])
    async def help(self, ctx: commands.Context):
        foscommand = []
        for command in self.commands:
            foscommand.append(command)
        await ctx.send(f"{str(foscommand)}")

async def load_cogs():
    for file in os.listdir(f"./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                forsenL.load_module(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

if __name__ == '__main__':
    forsenL = forsenL()
    asyncio.run(load_cogs())
    forsenL.run()  
