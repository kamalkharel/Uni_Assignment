import random 
import math

def game():
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

def playAgainHandler():
     playAgain = input('Please enter Y to play again or N to exit the game.')
     playAgain = playAgain.lower()
     if playAgain=='y': 
        game()
        #break functiong
        return
     elif playAgain=='n': 
         quit()
     else:
        #if user call anything but y or n, it will run the function again from the start
        print('Please Enter Correct Data.')
        playAgainHandler()
        return

def is_win(player, opponent):
     #will return true if the player wins against the computer
     #winning condition for the player: s>p, p>r and r>s 
     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player =='p' and opponent =='r'):
        return True
    
def game_best_of(n):
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
            print('It is a draw. You and computer both have choosen {}. \n'.format(user))
        
        elif result == 1:
            player_wins += 1
            #increment 
            print('You have chosen {} and the compiuter have chosen {}. You win \n'.format(user, computer))
        else:
            computer_wins += 1
            #increment 
            print('You chose {} and the computer chose {}. You lost :\n'.format(user, computer))
        print('\n')

    if player_wins > computer_wins:
        print('You have won the best of {} games! You are a champ'.format(n))
        playAgainHandler()
       


    else:
        print('Unfortunately. the computer has won the best out of {} games. Better luck next time!'.format(n))
        playAgainHandler()

if __name__ == '__main__':
    game_best_of(5) #Must win 5 times 

