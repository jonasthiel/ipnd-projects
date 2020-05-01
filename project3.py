"""
Created on Mon Sep 10 2018

@author: jonasthiel
"""

def gameHead():
	"""
	Starting point of the game: asking the user to input a game difficulty

	Input: gameDifficulty (str)

	Does not return anything
	"""
	gameDifficulty = raw_input("Please select a game difficulty by typing it in!" + "\n" + "Possible choices include easy, medium, and hard." + "\n")

	while gameDifficulty != "easy" and gameDifficulty != "medium" and gameDifficulty != "hard":
		print("Please enter only a game difficulty (easy, medium or hard) and nothing else!")
		gameDifficulty = raw_input()

	print("You've chosen " + gameDifficulty + "!" + "\n"*2 + "You've 5 chances per game." + "\n")

	gameText(gameDifficulty)

def gameText(gameDifficulty):
	"""
	Prints the text of the chosen game difficulty

	Input: gameDifficulty (str)

	Does not return anything

	Source: Credits to Carly Rae Jepsen, Arctic Monkeys and The Killers
	"""
	easy = """___1___, I just met you and this is crazy
But here's my number, so ___2___ me maybe
It's hard to look right at you baby
But here's my ___3___, so call me maybe
Hey I just met you and this is crazy
___4___ here's my number, so call me maybe
And all the other boys try ___5___ chase me
But here's my number, so call me maybe"""

	medium = """___1___ bet that you look good on the dance floor
I don't ___2___ if you're looking for romance or
I don't know what you're ___3___ for
I said, I bet that you look good on the ___4___ floor
Dancing to electro-pop like a robot from 1984
Well, from ___5___"""

	hard = """___1___, turning saints into the sea
Swimming through ___2___ lullabies, choking on your alibis
But it's ___3___ the price I pay, destiny is calling ___4___
Open up my eager eyes, 'cause I'm ___5___ Brightside"""

	if gameDifficulty == "easy":
		print(easy + "\n")
	elif gameDifficulty == "medium":
		print(medium + "\n")
	elif gameDifficulty == "hard":
		print(hard + "\n")

	gamePlay(gameDifficulty)

def gamePlay(gameDifficulty):
	"""
	Counts correct as well as incorrect answers

	Input: gameDifficulty (str), answer (str)

	Does not return anything
	"""
	counter = 1
	chances = 5
	while counter <= 5:
		if chances == 0:
			print("Game over!" + "\n"); restart(counter)
		else:
			answer = raw_input("What should be substituted in for ___" + str(counter) + "___?" + "\n")
			if gameAnswers(gameDifficulty, answer, counter) == True:
				print("Correct!"); counter += 1
				if counter == 6:
					print("Congratulations, you won!" + "\n"); restart(counter)
			else:
				print("That is incorrect. Try again!"); chances -= 1
				if chances > 1:
					print(str(chances) + " chances left!")
				else:
					print(str(chances) + " chance left!")

def gameAnswers(gameDifficulty, answer, counter):
	"""
	Checks the answer provided by the user for each game difficulty

	Input: gameDifficulty (str), answer (str), counter (int)

	Output: boolean
	"""
	substitutionEasy = ["Hey", "call", "number", "But", "to"]
	substitutionMedium = ["I", "know", "looking", "dance", "1984"]
	substitutionHard = ["Jealousy", "sick", "just", "me", "Mr."]
	if gameDifficulty == "easy":
		return answer == substitutionEasy[counter - 1]
	elif gameDifficulty == "medium":
		return answer == substitutionMedium[counter - 1]
	else:
		return answer == substitutionHard[counter - 1]

def restart(counter):
	"""
	Restarts the game if the user wants to

	Input: counter (int), restart (str)

	Does not return anything
	"""
	if counter == 6:
		restart = raw_input("Would you like to play again? Please answer with yes or no!" + "\n")
	else:
		restart = raw_input("Do you want to try again? Please answer with yes or no!" + "\n")
	while restart != "yes" and restart != "no":
		print("Please enter either yes or no and nothing else!")
		restart = raw_input()
	if restart == "yes":
		gameHead()
	else:
		print("Thanks for playing. Hope you come back soon!")
		exit()

gameHead()