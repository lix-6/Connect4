def show_board(board):
    print("+-----+-----+-----+-----+-----+-----+-----+")
    for row in board:
        print("| " + "  | ".join(row) + "  |")
        print("+-----+-----+-----+-----+-----+-----+-----+")
    print("|  A  |  B  |  C  |  D  |  E  |  F  |  G  |")
    print("+-----+-----+-----+-----+-----+-----+-----+")

def get_user_choice(next_position,kind): #next_position is a small list contains seven number:'5', after each input, the number will -1, when number=-1,the column is full. kind is 'X' or 'O'
    while True:
        user_input=input(f"player {turn}, please enter your choice,you need to enter a number between 1-7, if you want to leave, please enter q:").strip().lower()
        if user_input=="q":
            print("See you next time")
            break
        elif user_input.isalpha():
            print("Please use the integer number between 1-7 to denote A-G")
        elif int(user_input) not in [1,2,3,4,5,6,7]:
            print("You could only choose a integer number between 1-7")
        else:
            user_input=int(user_input)
            if next_position[user_input-1]==-1:
                print("The",user_input,"column is full, please change a column")
            else:
                return user_input-1
            
def choose_position(kind,column,board,next_position):
    row=next_position[column]
    board[row][column]=kind
    next_position[column]=next_position[column]-1

def check_win(board,column,next_position):
    row=next_position[column]+1
    kind=board[row][column]

    #check whether it's win in horizontal line--four chess pieces are in the same kind in one line
    count=1
    for j in range(1,4):
        if column+j<=6 and board[row][column+j]==kind or column-j>=0 and board[row][column-j]==kind:
            count=count+1
            if count==4:
                return True
    
    #check whether it's win in vertical line
    count=1
    for j in range(1,4):
        if row-j>=0 and board[row-j][column]==kind or row+j<=5 and board[row+j][column]==kind:
            count=count+1
            if count==4:
                return True

    #check whether it's win in top left to bottom right direction
    count=1
    for j in range(1,4):
        if row-j>=0 and column-j>=0 and board[row-j][column-j]==kind or row+j<=5 and column+j<=6 and board[row+j][column+j]==kind:
            count=count+1
            if count==4:
                return True

    #check whether it's win in top right to bottom left direction
    count=1
    for j in range(1,4):
        if row-j>=0 and column+j<=6 and board[row-j][column+j]==kind or row+j<=5 and column-j>=0 and board[row+j][column-j]==kind:
            count=count+1
            if count==4:
                return True
    return False

def check_full(next_position):
    for i in next_position:
        if next_position !=-1:
            return False
    return True

while True:
    board=[['  ' for _ in range (7)] for _ in range (6)]
    next_position=[5,5,5,5,5,5,5]
    turn=" X"
    print("Welcome to Connect 4")  #print menu
    print("1.New two-player Game")
    print("2.Exit")
    user_chioce=int(input("Enter your chioce:"))
    if user_chioce==1:
        while True:
            show_board(board)
            column=get_user_choice(next_position,turn)
            choose_position(turn,column,board,next_position)
            if check_win(board,column,next_position):
                show_board(board)               
                print("Player",turn,"won the game!")
                break
            elif check_full(next_position):
                show_board(board)
                print("The board is full, game over")
                break
            if turn==" X":
                turn=" O"
            else:
                turn=" X"
    if user_chioce==2:
        print("See you next time!")
        break
    if user_chioce!=1 and user_chioce!=2:
        print("Please enter 1 or 2")
    

