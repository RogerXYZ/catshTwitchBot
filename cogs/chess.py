"""
STILL UNDER DEVELOPMENT
"""
from twitchio.ext import commands
import chess as L
import asyncio

def print_board(boardd):
    board = boardd
    fors = ""
    forss = 0
    shit = str(board).strip(" ")
    shit += " "
    boarddd = []
    for item in shit:
        if item == ".":
            fors += " .. "
        else:
            fors += " " + item
        forss += 1
        if forss == 16:
            boarddd.append(fors)
            fors = ""
            forss = 0   
    return boarddd


class chess(commands.Cog):
    def __init__(self, forsenL: commands.Bot):
        self.forsenL = forsenL
        self.board = L.Board()

    @commands.command()
    async def chess(self, ctx: commands.Context, move):
        await ctx.send("This command is under development, please be patient Okayeg")
        


def prepare(forsenL: commands.Bot):
    forsenL.add_cog(chess(forsenL))
