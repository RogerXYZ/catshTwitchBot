from twitchio.ext import commands
import random

class general(commands.Cog):
    def __init__(self, forsenL: commands.Bot):
        self.forsenL = forsenL

    @commands.command()
    async def coinflip(self, ctx: commands.Context):
        hot = random.randint(0,1)
        if hot == 0:
            await ctx.send("Heads")
        else:
            await ctx.send("Tails")

    @commands.command(aliases= ["poro", "commands"])
    async def help(self, ctx: commands.Context):
        foscommand = []
        for command in self.commands:
            foscommand.append(command)
        await ctx.send(f"{str(foscommand)}")

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Hello {ctx.author.name}!")


def prepare(forsenL: commands.Bot):
    forsenL.add_cog(general(forsenL))