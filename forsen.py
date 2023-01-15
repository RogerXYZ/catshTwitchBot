"""
To add:
Cogs
Database for Logs
Artifact and CCU related commands
CCU Stock API
Chess API
NSFW commands
Tik Tac Toe
Dictionary API for word definitions ^query

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
        super().__init__(client_secret="e6yxm8mlnqxjpg3mydplg1blgqxfze", token="m180bp0wj88928u9z8z6xaftw3kvyn", prefix="^", initial_channels=["catsh", "rogerxyz", "redniii", "alastorkunn", "MayoAioli", "pambaulettox", "metser", "SaraTimberlain", "yosharpi", "MinusInsanity", "EddieHD_", "NaMTheWeebs", "alecbirdman", "FilunovicU", "swyfty_", "arozay", "HoldingKeys", "DheiddE", "Gerg"])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
#        forseee = message.content.find("https://")
        if message.echo:
            return
        elif message.content == ("forsen"):
            await message.channel.send("forsen")
        elif message.content == ("sigma"):
            await message.channel.send("sigma")
#        elif forseee != -1:
#            if message.channel.name == "rogerxyz":
#                with open("nsfw.txt", "a") as l:
#                    l.write("\n" + message.content[forseee:-1])
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