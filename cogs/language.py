from twitchio.ext import commands
import random
from wordhoard import Definitions

class language(commands.Cog):
    def __init__(self, forsenL: commands.Bot):
        self.forsenL = forsenL

    @commands.command()
    async def query(self, ctx: commands.Context, word):
        deff = Definitions(word).find_definitions()[0].strip()
        if word == "forsen":
            await ctx.send(f"{ctx.author.display_name}, Hans Eli Sebastian Fors (born 16 December 1990), known by the pseudonym Forsen, is a Swedish Twitch streamer who initially gained popularity for having competed in StarCraft II, but is best known for competing in Hearthstone and for streaming a variety of popular games.")
        elif word == "catshit":
            await ctx.send(f"KUKLE CATSHIT")
        elif len(deff) == 1:
            await ctx.send(f"{ctx.author.display_name}, there is no definition for '{word}'")
            return
        else:
            await ctx.send(f'{ctx.author.display_name}, {word} is defined as: "{deff}"')



def prepare(forsenL: commands.Bot):
    forsenL.add_cog(language(forsenL))