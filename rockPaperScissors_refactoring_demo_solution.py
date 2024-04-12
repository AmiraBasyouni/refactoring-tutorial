# *****************************************************************************/
# *    Title: Functions Refactor
# *    Author: Michele Pratusevich
# *    Date: 20 February 2022
# *    Availability: https://www.practicepython.org/exercise/2022/02/20/37-functions-refactor.html 
# ****************************************************************************/

def get_move(num):
    move = ""
    while move not in ["rock", "paper", "scissors"]:
        move = input("player{num} make your move (rock, paper, scissors): ")
    return move


def determine_winner(player1, player2):
    if player1 == player2:
        return "The outcome is a tie"
    elif (
        player1 == "rock"
        and player2 == "scissors"
        or player1 == "paper"
        and player2 == "rock"
        or player1 == "scissors"
        and player2 == "paper"
    ):
        return "player1 is the winner"
    else:
        return "player2 is the winner"
    


def rock_paper_scissors():
    while True:
    # get move of each player
        player1 = get_move(1)
        player2 = get_move(2)
    # determine winner
        winner_message = determine_winner(player1, player2)
        print(winner_message)
    # rematch?
        again = ""
        while again not in ["y", "n"]:
            again = input("Do you want to play again? (y/n): ")
        if again == "n":
            break

rock_paper_scissors()
