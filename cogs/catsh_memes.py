from twitchio.ext import commands
import random

class catsh_memes(commands.Cog):
    def __init__(self, forsenL: commands.Bot):
        self.forsenL = forsenL
        self.jokelist = ["What do you call a cow with no legs? Ground beef", "What do you call a fly with no wings? A walk", "Whats the deal with homeless people? Why dont they just get a house"]

    @commands.command()
    async def catsh_meme(self, ctx: commands.Context):
        await ctx.send("This command is under development, please be patient Okayeg")

    @commands.command()
    async def joke(self, ctx: commands.Context):
        ran = random.randint(0,(len(self.joke_list)-1))
        await ctx.send(self.joke_list[ran] + " LUL")

    @commands.command(aliases =["AddJoke", "Add_Joke"])
    async def addjoke(self, ctx: commands.Context, joke):
        approved_users = ["RogerXYZ", "catsh", "alecbirdman", "FrozenPepega"]
        if approved_users.index(ctx.message.author.display_name) == -1:
            await ctx.send("You do not have permission to utilize this command")
        if joke == None:
            await ctx.send('After calling the command, please enter your joke followed by the punchline in quotation marks. Example: "What do you call a cow with no legs? Ground beef"')
        else:
            self.jokelist.append(joke)

    @commands.command()
    async def vibE(self, ctx: commands.Context):
        await ctx.send(f"I want to break freee vibE https://youtu.be/WUOtCLOXgm8")

    @commands.command()
    async def catsh(self, ctx: commands.Context):
        await ctx.send(f"BANNED LULE")


    @commands.command(aliases= ["CCU", "about"])
    async def ccu(self, ctx: commands.Context):
        await ctx.send(f"The Catsh Cinematic Universe or Catsh Cuck Universe is an organization of content creators who work together in order to create catsh related content.")

def prepare(forsenL: commands.Bot):
    forsenL.add_cog(catsh_memes(forsenL))
