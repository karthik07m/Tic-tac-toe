# Draws the tic toc board
def draw_grid(mylist):
    print(mylist[0] + " | " + mylist[1] + " | " + mylist[2])
    print("----------")
    print(mylist[3] + " | " + mylist[4] + " | " + mylist[5])
    print("----------")
    print(mylist[6] + " | " + mylist[7] + " | " + mylist[8])


# Check's whether user is chosing valid position
def user_input_index():
    opt = " "
    while not(opt.isdigit()) or not(int(opt) in range(1, 10)):
        opt = input('Choose a index form 1-9: ')
        if opt.isdigit():
            if int(opt) in range(1, 10):
                pass
            else:
                print("Invalid number. Please enter a valid range")
        else:
            print("Please enter a digit")
    return int(opt)

# return's player 2 opt based on the player one selection
def get_p2_opt(p):
    if p == 'X':
        return 'O'
    else:
        return'X'

# check's who's turn is p1 or p2
def checkplayer(isp1):
    if isp1:
        return False
    else:
        return True

# return's player 
def get_opt_of_player(isp1, p1, p2):
    if isp1:
        return p1
    else:
        return p2

# check's any match of O or X
def check_winner(marker):
    return((mylist[0] == marker and mylist[1] == marker and mylist[2] == marker) or
    (mylist[3] == marker and mylist[4] == marker and mylist[5] == marker )or
    (mylist[3] == marker and mylist[4] == marker and mylist[5] == marker )or
    (mylist[6] == marker and mylist[7] == marker and mylist[8] == marker )or
    (mylist[0] == marker and mylist[3] == marker and mylist[6] == marker )or
    (mylist[1] == marker and mylist[4] == marker and mylist[7] == marker )or
    (mylist[2] == marker and mylist[5] == marker and mylist[8] == marker) or
    (mylist[0] == marker and mylist[4] == marker and mylist[8] == marker) or
    (mylist[2] == marker and mylist[4] == marker and mylist[6] == marker) )

# check whether game is draw
def check_game_draw(mylist):
    return " " not in mylist

# validates the user input. insert the X/O 
def insert_array(mylist):
    valid_input = True
    while valid_input:
        p1 = input("Choose X | O : ")
        print(p1)
        if p1 == 'X' or p1 == 'O':
             valid_input = False
        else:
            print('Please input a valid option')
           

    p2 = get_p2_opt(p1)

    print(f"Player 1 --> {p1}")
    print(f"Player 2 --> {p2}")
    isp1 = True
    is_any_winner = False

    while not(is_any_winner):
        print("   ")
        if isp1:
            print('Player 1 turn')
        else:
            print('Player 2 turn')
        index = user_input_index()
        marker = get_opt_of_player(isp1, p1, p2)
        mylist[index - 1] = marker
        draw_grid(mylist)
        isp1 = checkplayer(isp1)
        is_any_winner = check_winner(marker)
        if is_any_winner:
            if isp1:
                print("Congratulations p2 won !!")
            else:
                print("Congratulations p1 won !!")
        if check_game_draw(mylist):
            print("The game is draw")


#Intailze the tic toc boxes
mylist = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
draw_grid(mylist)
insert_array(mylist)
