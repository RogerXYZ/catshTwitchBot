from twitchio.ext import commands
import random
import json

class allah(commands.Cog):
    def __init__(self, forsenL: commands.Bot):
        self.forsenL = forsenL

    @commands.command()
    async def pray(self, ctx: commands.Context):
        phrase = ["جزاك الله خيرا", "يا رب", "يا ألله", "يا رب", "توكلنا على الله", "بارك الله فيك", "أعوذ بالله من الشيطان الرجيم", "أشهد أن لا إله إلا الله و أشهد أن محمد رسول الله","السلام عليكم و رحمة الله و بركاته","السلام عليكم","اللهم صلي على محمد","أستغفر الله", "إنا لله و إنا إليه راجعون","يرحمك الله","رحمك الله","إن شاء الله","بسم الله الرحمان الرحيم","بسم الله أوله و أخره","بسم الله","لا حول ولا قوة إلا بالله","الله أكبر","محمد رسول الله","لا إله إلا الله","ما شاء الله","سبحان الله","الحمد لله و الشكر لله", "الشكر لله","الحمد لله"]
        ran = random.randint(0,len(phrase)-1)
        await ctx.send(f"🕋 ThankEgg {ctx.message.author.display_name} prays to allah, {phrase[ran]}")
        with open("./prayer.json", "r") as e:
            forsen = json.load(e)
        try:
            num = forsen[ctx.author.display_name]
            num += 1
            forsen[ctx.author.display_name] = num
        except:
            forsen[ctx.author.display_name] = 1
        with open("./prayer.json", "w") as e:
            json.dump(forsen,e)

    @commands.command()
    async def chosen_one(self, ctx: commands.Context):
        with open("./prayer.json", "r") as e:
            forsen = json.load(e)
            maxx = max(forsen, key=forsen.get)
        await ctx.send(f"The most loyal muslim is: {maxx}, with having prayed {forsen[maxx]} times.")

def prepare(forsenL: commands.Bot):
    forsenL.add_cog(allah(forsenL))