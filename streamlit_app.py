import streamlit as st

# initialize the board
board = [' ' for _ in range(9)]

# define the function to print the board
def print_board():
    row1 = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    row2 = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row3 = '|{}|{}|{}|'.format(board[6], board[7], board[8])
    st.write(row1)
    st.write(row2)
    st.write(row3)

# define the function to check if a player has won
def check_win(player):
    # check rows
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    # check columns
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    # check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# define the main game function
def play_game():
    st.write("Welcome to Tic Tac Toe!")
    st.write("Player 1 will be X and Player 2 will be O.")
    st.write("The board is numbered from 1 to 9 as shown below:")
    st.write("|1|2|3|")
    st.write("|4|5|6|")
    st.write("|7|8|9|")
    player = 1
    while True:
        print_board()
        if player == 1:
            st.write("Player 1's turn")
        else:
            st.write("Player 2's turn")
        choice = st.number_input("Enter a number between 1-9: ", min_value=1, max_value=9, key=f"player_{player}")
        if board[choice-1] == ' ':
            if player == 1:
                board[choice-1] = 'X'
            else:
                board[choice-1] = 'O'
        else:
            st.write("That space is already taken!")
            continue
        if check_win('X'):
            print_board()
            st.write("Player 1 wins!")
            break
        if check_win('O'):
            print_board()
            st.write("Player 2 wins!")
            break
        if ' ' not in board:
            print_board()
            st.write("It's a tie!")
            break
        player = 2 if player == 1 else 1

# run the game
play_game()
