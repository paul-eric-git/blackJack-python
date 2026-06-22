import sys
from time import sleep
from random import shuffle
from random import choice


#helper methods, sorted alphabetically
def calculate_score(hand):

	#calculating the score of a hand provided via input, returns the score of the hand
	
	score = 0
	
	#this step is pretty ineffective
	for cards in hand:
		if(cards.startswith("Two")):
			score += 2
		elif(cards.startswith("Three")):
			score += 3
		elif(cards.startswith("Four")):
			score += 4
		elif(cards.startswith("Five")):
			score += 5
		elif(cards.startswith("Six")):
			score += 6
		elif(cards.startswith("Seven")):
			score += 7
		elif(cards.startswith("Eight")):
			score += 8
		elif(cards.startswith("Nine")):
			score += 9
		elif(cards.startswith("Ten") or cards.startswith("Jack") or cards.startswith("Queen") or cards.startswith("King")):
			score += 10
		elif(cards.startswith("Ace")):
			if(score + 11 > 21):
				score += 1
			else:
				score += 11
	return score	


def create_deck():

	#initialize card deck

	ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
	suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

	deck = []

	for rank in ranks:
		for suit in suits:
			deck += [f"{rank} of {suit}"]

	return deck
	

def deal_card(deck):

	#deals one card and returns the card + the updated deck
	
	card = choice(deck)
	
	deck.remove(card)

	return deck, card


def init_game(deck, player_hand, dealer_hand):

	#init game by dealing player 2 cards and the dealer 1 + "UNKNOWN" card and prints hands + scores
	#returns updated deck and both hands
		
	#adds 2 cards to players hand
	for _ in range(2):
		deck, card = deal_card(deck)
		player_hand.append(card)
	
	#adds one card and one "unknown" placeholder to dealers hand
	deck, card = deal_card(deck)
	dealer_hand.append(card)
	dealer_hand.append("UNKNOWN")
	
	#calculates scores
	player_score = calculate_score(player_hand)
	dealer_score = calculate_score(dealer_hand)
	dealer_score = str(dealer_score) + " + ?" 	
	
	#print hands + scores after game start
	print_scores(player_hand, player_score, dealer_hand, dealer_score)
	return deck, player_hand, player_score, dealer_hand, dealer_score
	

def print_scores(player_hand, player_score, dealer_hand, dealer_score):
	print("\n" + "Player: " + ", ".join(player_hand) + " -> Score: " + str(player_score))
	print("Dealer: " + ", ".join(dealer_hand) + " -> Score: " + str(dealer_score) + "\n")
	return		
	
def main():
	#init deck
	deck = create_deck()

	#shuffling the deck
	shuffle(deck)

	#init player and dealer hand + player score and dealer score
	player_hand = []
	dealer_hand = []

	#init_game
	deck, player_hand, player_score, dealer_hand, dealer_score = init_game(deck, player_hand, dealer_hand)

	#interactive player turn starts here
	players_turn = True

	while players_turn:
		#prompt user if an additional card is desired
		another_card = input("Another Card? (y/n): ").lower()		
		if another_card == "y":
			#draw new card, add it to player hand, calc player_score
			deck, card = deal_card(deck)
			player_hand.append(card)
			player_score = calculate_score(player_hand)
			
			#if score exceeds 21
			if(player_score > 21):
				print("Game Over, your score is: " + f"{player_score}" + "\nTherefore you lose.")
				sys.exit()
			#if score is lower than 21
			elif(player_score < 21):
				print_scores(player_hand, player_score, dealer_hand, dealer_score)
			#score is 21
			else:
				print_scores(player_hand, player_score, dealer_hand, dealer_score)
				print("BLACK JACK, you won!!!")
				sys.exit()
		elif another_card == "n":
			players_turn = False
		else:
			pass
	#dealers turn starts
	
	#unknown card needs to be exchanged
	dealer_hand.remove("UNKNOWN")
	deck, card = deal_card(deck)
	dealer_hand.append(card)
	dealer_score = calculate_score(dealer_hand)
	
	print_scores(player_hand, player_score, dealer_hand, dealer_score)
	sleep(3)

	dealers_turn = True
	while dealers_turn:
		
		sleep(3)
		
		if dealer_score < 17:
			deck, card = deal_card(deck)
			dealer_hand.append(card)
			
			dealer_score = calculate_score(dealer_hand)
			#print the scores
			print_scores(player_hand, player_score, dealer_hand, dealer_score)
		elif 17 <= dealer_score <= 21:
			dealer_score = calculate_score(dealer_hand)
			print_scores(player_hand, player_score, dealer_hand, dealer_score)
			dealers_turn = False
		else:
			print("Dealer went over 21, you won!!! Your Score: " + f"{player_score}")
			sys.exit()	
	
	#game end, this scenario happens, when dealers score is between 17 and 21 and player passed on his turn
	if player_score > dealer_score:
		print("\nYou won. Your Score: " + f"{player_score}, " + "Dealers Score: " + f"{dealer_score}")
	elif player_score < dealer_score:
		print("\nDealer won. Your Score: " + f"{player_score}, " + "Dealers Score: " + f"{dealer_score}")
	else:
		print("\nDraw! You both scored: " + f"{player_score}") 
	
	#print(deck)

main()
