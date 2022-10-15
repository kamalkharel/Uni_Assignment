"""System module."""
import random
import math
import sys

def game():
    """This function takes input."""
    user = input("Enter your choise. 'p' for paper, 's' for scissor and 'r' for rock")
    #for input and display
    user = user.lower()
    #To convert upper case into lower case

    computer = random.choice(['p','s','r'])
    #To generate random choice
    if user == computer:
        return (0, user, computer)
    #incase or draw
    if is_win(user, computer):
        return (1, user, computer)
    return (-1, user, computer)


def play_again_handler():
    """This function takes input."""
    play_again = input('Please enter Y to play again or N to exit the game.')
    play_again = play_again.lower()
    if play_again=='y':
        game_best_of(0)
        #break functiong
        return
    if play_again=='n':
        sys.exit()
    else:
        #if user call anything but y or n, it will run the function again from the start
        print('Please Enter Correct Data.')
        play_again_handler()
        return

def pr_check(player,opponent):
    """This function takes input."""
    return (player=='p' and opponent=='r')

def is_win(player, opponent):
    """This function takes input."""
    #will return true if the player wins against the computer
    #winning condition for the player: s>p, p>r and r>s
    return (player == 'r' and opponent == 's') or (player == 's'
    and opponent == 'p') or pr_check(player,opponent)

def game_best_of(num_score):
    """This function takes input."""
    #to fix match for certain rounds
    player_wins = 0
    #initial value of the player
    computer_wins = 0
    #initial value of the computer
    wins_necessary = math.ceil(5)
    #necessary to win 5 time to become the winner
    print(wins_necessary)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = game()
        #tie
        if result == 0:
            print(f"It is a draw. You and computer both have choosen {user}. \n")
        elif result == 1:
            player_wins += 1
            #increment
            print("You have chosen "+
            f"{user} and the compiuter have chosen {computer}. You win \n")
        else:
            computer_wins += 1
            #increment
            print(f"You chose {user}" + f"and the computer chose {computer}. You lost :\n")
        print('\n')

    if player_wins > computer_wins:
        print(f"You have won the best of {num_score} games! You are a champ")
        play_again_handler()
    else:
        print('Unfortunately.' +
        f"the computer has won the best out of {num_score} games. Better luck next time!")
        play_again_handler()
if __name__ == '__main__':
    game_best_of(5) #Must win 5 times
