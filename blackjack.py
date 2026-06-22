from random import shuffle
from random import choice


#helper methods, sorted alphabetically
def calculate_score(hand, score):

	#calculating the score of a hand provided via input, returns the score of the hand
	
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
	player_score = calculate_score(player_hand, 0)
	dealer_score = calculate_score(dealer_hand, 0)	
	
	#print hands + scores after game start
	print("Player: " + player_hand[0] + ", " + player_hand[1] + " -> Score: " + str(player_score))
	print("Dealer: " + dealer_hand[0] + ", " + dealer_hand[1] + " -> Score: " + str(dealer_score) + " + ?")

	return deck, player_hand, player_score, dealer_hand, dealer_score
	
		

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

	#interactive player part starts here
	players_turn = True

	while players_turn:
		#prompt user if an additional card is desired
		if input("Another Card? (y/n): ").lower() == "y":
			
			player_score = 0		
	
			#draw new card, add it to player hand, calc player_score
			deck, card = deal_card(deck)
			player_hand.append(card)
			player_score = calculate_score(player_hand, player_score)
			
			#if score exceeds 21
			if(player_score > 21):
				print("Game Over, Score: " + f"{player_score}")
				players_turn = False
			#if score is lower than 21
			elif(player_score < 21):
				print("Player: " + ", ".join(player_hand) + " -> Score: " +str(player_score))
			#score is 21
			else:
				print("BLACK JACK, you won!!!")
				players_turn = False
		else:
			players_turn = False
			
	#print(deck)

main()
