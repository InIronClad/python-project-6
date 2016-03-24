#Assignment: (Homework #6
#
#Completion Time: (4 hours)  
#In completing this program, I obtained help or worked with the following: 
#(Josh Shepherd, Zyante, python.org)

from random import *

#main function defined here
def main():

	print("*** Simple Blackjack ***")
	print("By Robert Crismon")
	play_game()
			
#play_game function defined here
def play_game():
	player_hand = 0
	computer_hand = 0
	card_value = 0
	hit_or_stand = " "
	busted = " "
	
	#player's turn
	while hit_or_stand != "s" and busted != "y":
		card_value = get_next_card_value()
		player_hand = player_hand + card_value
		print("The player is dealt a(n)", card_value)
		print("Your score is:", player_hand)
		if player_hand > 21:
			busted = "y"
			print("You busted! Better luck next time!")
			print("You lost!")
		else:
			hit_or_stand = input("Would you like to hit(h) or stand(s)?: ")
	hit_or_stand = ""
		
	#computer's turn
	while hit_or_stand != "s" and busted != "y":
		card_value = get_next_card_value()
		computer_hand = computer_hand + card_value
		print("The computer is dealt a(n)", card_value)
		print("The computer's score is: ", computer_hand)
		if computer_hand > 21:
			busted = "y"
			print("The computer busted!")
			print("You Win!")
		elif computer_hand < 17:
			print("The computer's score is below 17 and takes another card.")
		elif computer_hand >= 17:
			hit_or_stand = "s"
			print("The computer stands.")
	
	#determines who wins if player or computer do not bust
	if player_hand > computer_hand and player_hand <= 21:
		print("You win!")
	elif player_hand < computer_hand and computer_hand <= 21:
		print("You lose!")
	#this handles the rare but possible occurrance of a draw
	elif player_hand == computer_hand:
		print("A draw occurred. No one wins.")

#get_next_card_value function defined here		
def get_next_card_value():
	card_value = randint(2, 11)
	return card_value
			

play_again = ""
#main function started
main()
play_again = input("Would you like to play again (y/n)?: ")#play_again reset here
while play_again != "n":		
	play_game()	
	play_again = input("Would you like to play again (y/n)?: ")#play_again reset here as well
