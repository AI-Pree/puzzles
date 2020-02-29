import functools
clues = ( 3, 2, 2, 3, 2, 1,
          1, 2, 3, 3, 2, 2,
          5, 1, 2, 2, 4, 3,
          3, 2, 1, 2, 2, 4)

N = len(clues)/4 #square always gonna have 4 sides
building = [1,2,3,4,5,6]

top = clues[:N]
left = clues[N:2*N]
bot = clues[N*3-1:N*2-1:-1]
right = clues[-1:N*3-1:-1]
grid = [["-" for i in range(6)] for row in range(6)]

#fill all the cell with 6 whose top, left, bot and top clues is 1
grid[0][top.index(1)] = 6 #for top clue
grid[N-1][bot.index(1)] = 6 #for bot clue
grid[left.index(1)][N-1] = 6 #for left clue
grid[right.index(1)][0] = 6 #for right clue

#for top
if 6 in top:
    for i in range(1,N+1):
        grid[i][top.index(6)] = i

if 6 in bot:
    for i, c in enumerate(range(N-1,-1,-1)):
        grid[c][top.index(6)] = i + 1

if 6 in left:
    for i,c in enumerate(range(N-1,-1,-1)):
        grid[left.index(6)][i] = i+1

if 6 in right:
    for i in range(N):
        grid[right.index(6)][i] = i 

for r in grid:
    for c in r:
        print(c, end =" ")
    print("",end = "\n")
    

#-----------------------Viewable skyscrapers---------------------------------#

#given the row, gets the numbers of skyscrapers that can be viewed from right
def from_right(row:int)->int:
    return clues[N+row-1]

#given the row, gets the numbers of skyscrapers that can be viewed from left
def from_left(row:int)->int:
    return clues[-row]

#given the col, gets the numbers of skyscrapers that can be viewed from bot
def from_bot(col:int)->int:
    return clues[2*N+col]

#given the col, gets the numbers of skyscrapers that can be viewed from top
def from_top(col:int)->int:
    return clues[col]


    #-----------------Gets the numbers of skyscrapers viewable-----------------------#
    #---------------------------for checking purpose---------------------------------#

    #goes from top to bottom of the given cell
    def topToBot(col:int)->list:
        return [grid[r][col] for r in range(0, N)]

    #goes from top to bottom of the given cell
    def botToTop(col:int)->list:
        return [grid[r][col] for r in range(N,-1,-1)]
            
    #goes from top to bottom of the given cell
    def leftToRight(row:int)->list:
        return [grid[row][c] for c in range(N)]

    #goes from top to bottom of the given cell
    def rightToLeft(row:int)->list:
        return [grid[row][c] for c in range(N-1,-1,-1)]

    #count the skyscrapers fromt the list value received from function rightToLeft, leftToRight, botToTop and topTopBot
    def countSky(mylist:list)->int:
        m = mylist[0] # max value
        count = 0
        for i in mylist[1:]:
            if m < i:
                m = i
                if m == 6:
                    break
                count += 1
        return count
        


def solve(clues):
    pass

