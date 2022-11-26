"""
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]


To print the board
input: none
Output: none

def printboard(board):
    for row in board:
        for slot in row:
            print(f"{slot}", end="")
        print()

printboard(board)

To quit the game
input: q
output: Thanks for playing


def quit(user_input):
    if user_input == "q": 
        print("Thanks for playing")
        return True
    else: return False

To check whether the inputed number is within the boundaries(1-9)
input : number
output: check true or false

def input_check(user_input):
    if not isnum(user_input): return False
    user_input = int(user_input)
    if not boundaries(user_input): return False
    return True
    
"""

"""
def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number>")
        return False
    else: return True

def boundaries(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is not within boundaries")
        return False
    else: return True

def taken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else: return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row,col)

while True:
    user_input = input("Please enter a position 1-9 or enter \"q\" to quit:")
    if quit(user_input): break
    if not input_check(user_input):
        print("try again:(")
        continue
    user_input = int(user_input)- 1
    coords = coordinates(user_input)
    board[0][0] = "x"
    if taken(coords, board):
        print("Please try again.")
        continue
"""
print ("Coordinates :(a,b,c)(1,2,3) ex: a1")
a1 = ""
a2 = ""
a3 = ''
b1 = ''
b2 = ''
b3 = ''
c1 = ''
c2 = ''
c3 = ""
winner = 0 # 0: no Winner;  1:X 2: O

def DebugFns(x):
    print (str(x) + str(type(x)))
    print (x)
    print (OutputFns())




def InputFns():
    global a1, a2, a3
    global b1, b2, b3
    global c1, c2, c3
    
    p1 = input("Player 1, X, Enter a coordinate:")
    
    if p1 == "a1":
        a1 = 'X'
    if p1 == "a2":
        a2 = 'X'
    if p1 == "a3":
        a3 = 'X'
    if p1 == "b1":
        b1 = 'X'
    if p1 == "b2":
        b2 = 'X'
    if p1 == "b3":
        b3 = 'X'
    if p1 == "c1":
        c1 = 'X'
    if p1 == "c2":
        c2 = 'X'
    if p1 == "c3":
        c3 = 'X'
    p2 = input("Player 2, O, Enter a coordinate:")
   
    if p2 == "a1":
        a1 = 'O'
    if p2 == "a2":
        a2 = 'O'
    if p2 == "a3":
        a3 = 'O'
    if p2 == "b1":
        b1 = 'O'
    if p2 == "b2":
        b2 = 'O'
    if p2 == "b3":
        b3 = 'O'
    if p2 == "c1":
        c1 = 'O'
    if p2 == "c2":
        c2 = 'O'
    if p2 == "c3":
        c3 = 'O'

def ProcessFns():
    global winner
    if a1 == "X" and a2 == "X" and a3 == "X":
        print ("Player one WINS")
        winner = 1 
    if b1 == "X" and b2 == "X" and b3 == "X":
        print ("Player one WINS")
        winner = 1 
    if c1 == "X" and c2 == "X" and c3 == "X":
        print ("Player one WINS")
        winner = 1 

    if a1 == "X" and b1 == "X" and c1 == "X":
        print ("Player one WINS")
        winner = 1 

    if a2 == "X" and b2 == "X" and c2 == "X":
        print ("Player one WINS")
        winner = 1 

    if a3 == "X" and b3 == "X" and c3 == "X":
        print ("Player one WINS")
        winner = 1 

    if a1 == "X" and b2 == "X" and c3 == "X":
        print ("Player one WINS")
        winner = 1 

    if a3 == "X" and b2 == "X" and c1 == "X":
        print ("Player one WINS")
        winner = 1 

#player 2
    if a1 == "O" and a2 == "O" and a3 == "O":
        print ("Player two WINS")
        winner = 2 

    if b1 == "O" and b2 == "O" and b3 == "O":
        print ("Player two WINS")
        winner = 2 

    if c1 == "O" and c2 == "O" and c3 == "O":
        print ("Player two WINS")
        winner = 2 

    if a1 == "O" and b1 == "O" and c1 == "O":
        print ("Player two WINS")
        winner = 2 

    if a2 == "O" and b2 == "O" and c2 == "O":
        print ("Player two WINS")
        winner = 2 

    if a3 == "O" and b3 == "O" and c3 == "O":
        print ("Player two WINS")
        winner = 2 

    if a1 == "O" and b2 == "O" and c3 == "O":
        print ("Player two WINS")
        winner = 2 

    if a3 == "O" and b2 == "O" and c1 == "O":
        print ("Player two WINS")
        winner = 2 

    #else:
    #    print("TIE")


"""
Only do the printing. NO assignment
"""

def OutputFns():
  global a1, a2, a3
  global b1, b2, b3
  global c1, c2, c3
  print( ' ' + a1 + ' ' + '|' + ' '+ a2 + ' ' +'|' + ' '+ a3+ ' ')
  print("___________")
  print( ' ' + b1 + ' ' + '|' + ' '+ b2 + ' ' +'|' + ' '+ b3+ ' ')
  print("___________")
  print( ' ' + c1 + ' ' + '|' + ' '+ c2 + ' ' +'|' + ' '+ c3+ ' ')
  #print(a1"l"a2"l"a3)

i = 0
while winner == 0:
    InputFns()
    ProcessFns()
    OutputFns()
    i=i+1

print("winner is Player" + str(winner))
                       
    
