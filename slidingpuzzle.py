#Created by Steven Sugihermanto
from random import shuffle
import sys

g_data = [1, 2, 3, 4, 5, 6, 7, 8, '_']
g_win = [1, 2, 3, 4, 5, 6, 7, 8, '_']

try:
    input("Press Enter key to play!!! >>> ")
except SyntaxError:
    pass

def number_randomizer(data):
    shuffle(data)
    return data

g_new = number_randomizer(g_data)
print(g_new)
def inversion():
    global g_new
    g_new[g_new.index("_")] = 0
    inv_count = 0
    for x in range(0,8):
        for y in range(x+1, 9):
            if y < g_new[x] and y > 0:
                inv_count += 1
    g_new[g_new.index(0)] = "_"
    return inv_count

def solvable():
    global g_new
    inversion()
    while True:
        if inversion() % 2 == 0:
            return (inversion() % 2 == 0)
        else:
            g_new = number_randomizer(g_data)
            return

def left():
    current = g_new.index("_")
    change = g_new.index("_") + 1
    if -1 < change < 9:
        if change != 3 and change != 6:
            g_new[change], g_new[current] = g_new[current], g_new[change]
        else:
            print("Invalid Move!")
    else:
            print("Invalid Move!")

def right():
    current = g_new.index("_")
    change = g_new.index("_") - 1
    if -1 < change < 9:
        if change != 2 and change != 5:
            g_new[change], g_new[current] = g_new[current], g_new[change]
        else:
            print("Invalid Move!")
    else:
        print("Invalid Move!")

def up():
    current = g_new.index("_")
    change = g_new.index("_") + 3
    if -1 < change < 9:
        g_new[change], g_new[current] = g_new[current], g_new[change]
    else:
        print("Invalid Move!")

def down():
    current = g_new.index("_")
    change = g_new.index("_") - 3 
    if -1 < change < 9:
        g_new[change], g_new[current] = g_new[current], g_new[change]
    else:
        print("Invalid Move!")

def board():
    global g_new
    c = 0
    for index in range(len(g_new)):
        print(g_new[index], end=' ')
        c += 1
        if c == 3:
            print('\n', end='')
            c -= 3
                    
def movement():
    play = input("Input sliding movement (l, r, u, d): ")
    print("---------------------------------------------")
    if play == "l":
        left()
    elif play == "r":
        right()
    elif play == "u":
        up()
    elif play == "d":
        down()
    elif play != "#CHEAT":
        play = "x"
    return play

def game():
    global g_new
    counter = 0
    solvable()
    while True:
        board()
        play = movement()
        if play == "#CHEAT":
            print("1..."," 2..","  3."," ", sep="\n", end ="\n")
            g_new = g_win
        elif play == "x":
            print("Wrong Input!")       
            continue
        counter += 1
        while g_new == g_win:
            board()
            print("Congratulation!!!","\n", "You have finished the puzzle in", counter, "steps.")
            while True:
                again = input("Do you want to play again (y/n): ")
                if again == "n":
                    print("Thankyou for playing see you again next time!")  
                    sys.exit()
                if again == "y":
                    g_new = number_randomizer(g_data)
                    counter = 0
                    game()
                else: print("Wrong Input!")
            break
        
game()
# type "#CHEAT" to finished the game.
