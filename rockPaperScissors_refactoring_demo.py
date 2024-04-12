# *****************************************************************************/
# *    Title: Functions Refactor
# *    Author: Michele Pratusevich
# *    Date: 20 February 2022
# *    Availability: https://www.practicepython.org/exercise/2022/02/20/37-functions-refactor.html 
# ****************************************************************************/

while True:
	player1 = ""
	while player1 not in ["rock", "paper", "scissors"]:
		player1 = input("player1 make your move (rock, paper, scissors): ")
	player2 = ""
	while player2 not in ["rock", "paper", "scissors"]:
		player2 = input("player2 make your move (rock, paper, scissors): ")
	winner_message = ""
	if player1 == player2:
		winner_message = "The outcome is a tie"
	elif player1 == "rock" and player2 == "scissors":
		winner_message = "player1 is the winner"
	elif player1 == "paper" and player2 == "rock":
		winner_message = "player1 is the winner"
	elif player1 == "scissors" and player2 == "paper":
		winner_message = "player1 is the winner"
	elif player2 == "rock" and player1 == "scissors":
		winner_message = "player2 is the winner"
	elif player2 == "paper" and player1 == "rock":
		winner_message = "player2 is the winner"
	elif player2 == "scissors" and player1 == "paper":
		winner_message = "player2 is the winner"
	print(winner_message)
	again = ""
	while again not in ["y", "n"]:
		again = input("Do you want to play again? (y/n): ")
	if again == "n":
		break