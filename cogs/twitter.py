from twitchio.ext import commands
import tweepy
import json
import random

class twitter(commands.Cog):
    def __init__(self, forsenL: commands.Bot):
        self.forsenL = forsenL

        self.auth = tweepy.OAuth1UserHandler(
        "U93PbVgGNftCKNUUifC63yvlv",
        "3JhFAnCksVo7hhLYREdevOme5oTgTwNa2N5N62MQ8mPIDJdpp9",
        "1238565422816849920-PG6xhRVNQe4rt7PgpIMjtz8kC03NAE",
        "RfigAHsZdTXSWT5hToOc4xvS5XblulkBwUOa1s7CCxYF4"
        )
    
        self.api = tweepy.API(self.auth)

    @commands.command(aliases= ["POGGIES", "poggies"])
    async def FeelsWowMan(self, ctx: commands.Context, forsenn = None):
        creators = ["ADC_Vr", "Miwa_Satomiii", "TEAR_VR", "Sara26491189", "Lamire_Vrc", "Nya_Sukida", "VRC_ginsan", "kaoruco_vrc", "keke_VRchat", "kpmrlove"]
        poggies = []
        for creator in creators:
            for baj in tweepy.Cursor(self.api.search_tweets, q = f"from:{creator} -filter:retweets filter:images").items(11):
                dog = json.dumps(baj._json)
                catsh =json.loads(dog)
                try:
                    forsen = catsh["entities"][0]["media"][0]["media_url"]
                except:
                    try:
                        forsen = catsh["entities"]["media"]["media_url"]
                    except:
                        try:
                            forsen = catsh["entities"][0]["media"]["media_url"]
                        except:
                            try:
                                forsen = catsh["entities"]["media"][0]["media_url"]
                            except:
                                continue
                poggies.append(forsen)
        ran = random.randint(0,(len(poggies)-1))
        if forsenn == None:
            await ctx.send(f"{ctx.author.display_name}, {poggies[ran]}")
        else:
            await ctx.send(f"{forsenn}, {poggies[ran]}")

    @commands.command(aliases= ["POGGERS", "poggers"])
    async def honkers(self, ctx: commands.Context):
        """
        creators = ["forsen"]
        poggies = []
        for creator in creators:
            for baj in tweepy.Cursor(self.api.search_tweets, q = f"from:chengzimiaoj").items(100):
                dog = json.dumps(baj._json)
                catsh =json.loads(dog)
                #theories: not puting links in the same "media url" that i have been using which would indeed cause some of these errors or it is something related to an nsfw filter
                try:
                    forsen = catsh["entities"][0]["media"][0]["media_url"]
                except:
                    try:
                        forsen = catsh["entities"]["media"]["media_url"]
                    except:
                        try:
                            forsen = catsh["entities"][0]["media"]["media_url"]
                        except:
                            try:
                                forsen = catsh["entities"]["media"][0]["media_url"]
                            except:
                                print("fatal error")
                                continue
                print(catsh)
                poggies.append(forsen)
        ran = random.randint(0,(len(poggies)-1))
        print(poggies)
        await ctx.send(f"{ctx.author.display_name}, {poggies[ran]}")
        """
        await ctx.send("This command is under development, please be patient Okayeg")
def prepare(forsenL: commands.Bot):
    forsenL.add_cog(twitter(forsenL))
