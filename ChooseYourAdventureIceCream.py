import random
import time



def choosePlayerNumber():
	# while num_players isn't a number ask for a number
	print('How many people are sharing this ice cream?')
	num_players = raw_input()
	return num_players

def displayIntro():
	print('You and your friends bought an ice cream cone')
	print('The store only had one cone left')
	print('You are going to have to share')
	print('')
	print('As you pass the ice cream around you can either')
	print('lick it or bite it')
	print('')
	print('You DO NOT want to be the greedy one to eat the last bit')
	print('Choose carefully! Sharing is caring!')
	print('')

def eatIceCream(num_players, turn):
	numberLicks = random.randint(1, 10)
	
	playerAction = playerTurn(turn)
	
	#TO-DO check for invalid input

	#subtract action
	if playerAction == '1':
		numberLicks = numberLicks - 1
	else:
		numberLicks = numberLicks - 2

	#check if 0
	if (numberLicks <= 0):
		print('Player ' + str(turn) + ', You Lose!')
		print('You ate all the ice cream!')
	else:
		turn = ((turn % int(num_players)) + 1)
		eatIceCream(num_players, turn)

def playerTurn(turn):
	print('')
	print('Player ' + str(turn))
	time.sleep(1)
	print('The ice cream is passed to you...')
	time.sleep(1)
	print('Your mouth begins to water...')
	time.sleep(1)
	print('It is your favorite flavor!!')
	time.sleep(1)
	print('What do you do? Lick it (1) or Bite it (2)')
	playerAction = raw_input()

	return playerAction


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

	displayIntro()

	turn = int(1)
	
	num_players = choosePlayerNumber()
	print('')

	eatIceCream(num_players, turn)

	print('Do you want to play again? (yes or no)')
	playAgain = raw_input()
