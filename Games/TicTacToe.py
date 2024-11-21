import turtle as trtl
import random

# Setup
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic('r.png')

circle = trtl.Turtle()
x = trtl.Turtle()

# Available spots on the board
available_spots = [7, 8, 9, 4, 5, 6, 1, 2, 3]

# To track the positions of 'O' (player) and 'X' (computer)
player_moves = []  # Player (O) positions
computer_moves = []  # Computer (X) positions

# Winning combinations (rows, columns, diagonals)
winning_combinations = [
    [7, 8, 9],  # Top row
    [4, 5, 6],  # Middle row
    [1, 2, 3],  # Bottom row
    [7, 4, 1],  # Left column
    [8, 5, 2],  # Middle column
    [9, 6, 3],  # Right column
    [7, 5, 3],  # Diagonal top-left to bottom-right
    [9, 5, 1],  # Diagonal top-right to bottom-left
]

# Define spot coordinates for turtle
spots = {
    7: (-250, 145),
    8: (0, 145),
    9: (250, 145),
    4: (-250, -80),
    5: (0, -80),
    6: (250, -80),
    1: (-250, -350),
    2: (0, -350),
    3: (250, -350),
}

# Draw X (computer) on the board
def draw_x(position):
    x.penup()
    x.goto(spots[position])
    x.pendown()
    x.write("X", align='center', font=("Arial", 135, "bold"))

# Draw O (player) on the board
def draw_o(position):
    circle.penup()
    circle.goto(spots[position])
    circle.pendown()
    circle.pensize('20')
    circle.circle(75)

# Make player's move
def make_player_move(position):
    draw_o(position)
    player_moves.append(position)  # Track player's move
    available_spots.remove(position)  # Mark the spot as used
    check_win(player_moves, "Player (O)")  # Check if player wins

# Make computer's move
def make_computer_move():
    if available_spots:
        position = random.choice(available_spots)  # Pick a random available spot
        draw_x(position)
        computer_moves.append(position)  # Track computer's move
        available_spots.remove(position)  # Mark the spot as used
        check_win(computer_moves, "Computer (X)")  # Check if computer wins

# Check for a win
def check_win(moves, player):
    for combo in winning_combinations:
        if all(position in moves for position in combo):
            display_winner(player)
            return True
    return False

# Display winner
def display_winner(player):
    print(f"{player} wins!")
    circle.hideturtle()
    x.hideturtle()
    wn.bye()  # Close the window

# Slot functions to handle player moves
def Slot7():
    if 7 in available_spots:
        make_player_move(7)
        make_computer_move()

def Slot8():
    if 8 in available_spots:
        make_player_move(8)
        make_computer_move()

def Slot9():
    if 9 in available_spots:
        make_player_move(9)
        make_computer_move()

def Slot4():
    if 4 in available_spots:
        make_player_move(4)
        make_computer_move()

def Slot5():
    if 5 in available_spots:
        make_player_move(5)
        make_computer_move()

def Slot6():
    if 6 in available_spots:
        make_player_move(6)
        make_computer_move()

def Slot3():
    if 3 in available_spots:
        make_player_move(3)
        make_computer_move()

def Slot2():
    if 2 in available_spots:
        make_player_move(2)
        make_computer_move()

def Slot1():
    if 1 in available_spots:
        make_player_move(1)
        make_computer_move()

# Keyboard bindings for slots
wn.onkeypress(Slot7, '7')
wn.onkeypress(Slot8, '8')
wn.onkeypress(Slot9, '9')
wn.onkeypress(Slot4, '4')
wn.onkeypress(Slot5, '5')
wn.onkeypress(Slot6, '6')
wn.onkeypress(Slot1, '1')
wn.onkeypress(Slot2, '2')
wn.onkeypress(Slot3, '3')

wn.listen()

wn.mainloop()