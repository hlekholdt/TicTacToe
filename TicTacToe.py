#%%
def author():
    return 'Liv Ekholdt'
#%%
from random import randint
import random
import copy
# %%
def DrawBoard(Board):
    '''
    Parameter: Board is a 3x3 matrix (a nested list).
    Return: None
    Description: this function prints the chess board    
    hint: Board[i][j] is ' ' or 'X' or 'O' in row-i and col-j
          use print function
    '''
    print(Board[0][0], "|", Board[0][1], "|", Board[0][2])
    print("--+---+--")
    print(Board[1][0], "|", Board[1][1], "|", Board[1][2])
    print("--+---+--")
    print(Board[2][0], "|", Board[2][1], "|", Board[2][2])

#%% 
def IsSpaceFree(Board, i ,j):
    '''
    Parameters: Board is the game board, a 3x3 matrix
                i is the row index, j is the col index
    Return: True or False
    Description: 
        return True  if Board[i][j] is empty ' '
        return False if Board[i][j] is not empty
        return False if i or j is invalid (e.g. i = -1 or 100)
    '''
    if Board[i][j] == ' ':
        return True
    elif (i<0 or j<0 or i>=3 or j>=3):
        return False
    else:
        return False
    
#%%
def GetNumberOfChessPieces(Board):
    '''
    Parameters: Board is the game board, a 3x3 matrix
    Return: the number of chess pieces on Board
            i.e. the total number of 'X' and 'O'
    hint: define a counter and use a nested for loop, like this
          for i in 0 to 3
              for j in 0 to 3
                  add one to the counter if Board[i][j] is not empty
    '''
    counter = 0
    for r in range(3):
        for c in range(3):
            if(Board[r][c] != " "):
                counter += 1
    
    return counter
    
    
#%%
def IsBoardFull(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    if(GetNumberOfChessPieces(Board)==9):
        return True
    return False
    
    
#%%
def IsBoardEmpty(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    if(GetNumberOfChessPieces(Board)==0):
        return True
    return False
    
    
#%%
def UpdateBoard(Board, Tag, Choice):
    '''
    Parameters: 
        Board is the game board, a 3x3 matrix
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag
    '''
    r = Choice[0]
    c = Choice[1]
    
    Board[r][c] = Tag
    
#%%
def HumanPlayer(Tag, Board):
    '''
    Parameters:        
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
    while(True):
        while(True):
            try:
                humanRow = int(input("Enter row: "))
                if(humanRow > 2 or humanRow < 0):
                    print("Invalid input. 3x3 Matrix.")
                    continue
                break
            except:
                print("Invalid input.")
        
        while(True):
            try:
                humanCol = int(input("Enter column: "))
                if(humanCol > 2 or humanCol < 0):
                    print("Invalid input. 3x3 Matrix.")
                    continue
                break
            except:
                print("Invalid input.")
        if (IsSpaceFree(Board, humanRow, humanCol) == False):
            print("That spot is already taken!")
        else:
            break
        
    return (humanRow,humanCol)
    
#%%
def ComputerPlayer(Tag, Board):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
    Description:
        ComputerPlayer will choose an empty spot on the board
        a random strategy in a while loop:
            (1) randomly choose a spot on the Board
            (2) if the spot is empty then return the choice (row, col)
            (3) if it is not empty then go to (1)
    Attention:
        Board is NOT modified in this function
    '''
    
    while True:
        randRow = randint(0,2)
        randCol = randint(0,2)
        if (IsSpaceFree(Board, randRow, randCol) == True):
            return (randRow,randCol)
        else:
            continue
    
    
#%%
def Judge(Board):
    '''
    Parameters:
         Board is the current game board, a 3x3 matrix
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    hint:
        (1) check if anyone wins, i.e., three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
        (2) if no one wins, then check if it is a tie
                i.e. if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress
    '''
    
    if (Board[0][0]=='X' and Board[0][1]=='X' and Board[0][2]=='X') or (Board[1][0]=='X' and Board[1][1]=='X' and Board[1][2] == 'X') or (Board[2][0]=='X' and Board[2][1]=='X' and Board[2][2]=='X'):
        return 1
        #this is all 3 in a row
    elif (Board[0][0]=='X' and Board[1][0]=='X' and Board[2][0]=='X') or (Board[0][1]=='X' and Board[1][1]=='X' and Board[2][1] == 'X') or (Board[0][2]=='X' and Board[1][2]=='X' and Board[2][2]=='X'):
        return 1
        #this is all 3 in a column
    elif (Board[0][0]=='X' and Board[1][1]=='X' and Board[2][2]=='X') or (Board[0][2]=='X' and Board[1][1]=='X' and Board[2][0]=='X'):
        return 1
        ##this if for the diagonals
    elif (Board[0][0]=='O' and Board[0][1]=='O' and Board[0][2]=='O') or (Board[1][0]=='O' and Board[1][1]=='O' and Board[1][2] == 'O') or (Board[2][0]=='O' and Board[2][1]=='O' and Board[2][2]=='O'):
        return 2
        #this is all 3 in a row
    elif (Board[0][0]=='O' and Board[1][0]=='O' and Board[2][0]=='O') or (Board[0][1]=='O' and Board[1][1]=='O' and Board[2][1] == 'O') or (Board[0][2]=='O' and Board[1][2]=='O' and Board[2][2]=='O'):
        return 2
        #this is all 3 in a column
    elif (Board[0][0]=='O' and Board[1][1]=='O' and Board[2][2]=='O') or (Board[0][2]=='O' and Board[1][1]=='O' and Board[2][0]=='O'):
        return 2
        ##this if for the diagonals
    elif IsBoardFull(Board)==True:
        return 3
    else:
        return 0
    
    
#%%
def ShowOutcome(Outcome, NameX, NameO):
    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''
    if(Outcome==0):
        print("the game is still in progress")
    elif(Outcome==1):
        print(NameX,"wins")
    elif(Outcome==2):
        print(NameO,"wins")
    else:
        print("it is a tie!")
    
    
    
#%% read but do not modify this function
def Which_Player_goes_first():
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.  
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print("Computer player goes first")
        PlayerX = ComputerPlayer        
        PlayerO = HumanPlayer     
    else:
        print("Human player goes first")
        PlayerO = ComputerPlayer        
        PlayerX = HumanPlayer           
    return PlayerX, PlayerO
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Welcome to Tic Tac Toe Game")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order of the players
    PlayerX, PlayerO = Which_Player_goes_first()
    # get the name of each function object
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    # (1)  get the choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board)
    # (2)  update the Board
    # (3)  draw the Board
    # (4)  get the outcome from Judge
    # (5)  show the outcome
    # (6)  if the game is completed (win or tie), then break the loop
    # (7)  get the choice from PlayerO
    # (8)  update the Board
    # (9)  draw the Board
    # (10) get the outcome from Judge
    # (11) show the outcome
    # (12) if the game is completed (win or tie), then break the loop
    #---------------------------------------------------
    # your code starts from here
    while True:
        playerXChoice = PlayerX('X',Board)
        UpdateBoard(Board,'X',playerXChoice)
        DrawBoard(Board)
        theOutcome = Judge(Board)
        ShowOutcome(theOutcome,NameX,NameO)
        if(theOutcome != 0):
            break
        playerOChoice = PlayerO('O',Board)
        UpdateBoard(Board,'O',playerOChoice)
        DrawBoard(Board)
        theOutcome = Judge(Board)
        ShowOutcome(theOutcome,NameX,NameO)
        if(theOutcome != 0):
            break
    
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()
