from twitchio.ext import commands
import random

class catsh_memes(commands.Cog):
    def __init__(self, forsenL: commands.Bot):
        self.forsenL = forsenL

    @commands.command()
    async def catsh_meme(self, ctx: commands.Context):
        await ctx.send("This command is under development, please be patient Okayeg")

    @commands.command(aliases= ["ingame", "Ingame"])
    async def InGame(self, ctx: commands.Context):
        if ctx.channel.name == "catsh":
            await ctx.send("monkaLaugh this command is not enabled on this channel")
        await ctx.send(f"@{ctx.author.display_name} you're a black person, in game InGame")

    @commands.command()
    async def joke(self, ctx: commands.Context):
        joke_list = {0 :"What do you call a cow with no legs? Ground beef", 1: "What do you call a fly with no wings? A walk", 2: "Whats the deal with homeless people? Why dont they just get a house"}
        ran = random.randint(0,(len(joke_list)-1))
        await ctx.send(joke_list[ran] + " LUL")

    @commands.command()
    async def vibE(self, ctx: commands.Context):
        await ctx.send(f"I want to break freee vibE https://youtu.be/WUOtCLOXgm8")


def prepare(forsenL: commands.Bot):
    forsenL.add_cog(catsh_memes(forsenL))