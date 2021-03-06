# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 12

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
	word_length = len(word)
	if word_length == 0:
		return 0
	else:
		word_in_lowercase = word.lower()
		first_part_score = 0
		second_part_score = 0
		#first component 
		for char in word_in_lowercase:
			first_part_score += SCRABBLE_LETTER_VALUES[char]
		#second component
		if 7*word_length - 3*(n - word_length) > 1:
			second_part_score = 7*word_length - 3*(n - word_length)
		else:
			second_part_score = 1
		#total score
		total_word_score = first_part_score * second_part_score
		return total_word_score

	"""
	Returns the score for a word. Assumes the word is a
	valid word.
	
	You may assume that the input word is always either a string of letters, 
	or the empty string "". You may not assume that the string will only contain 
	lowercase letters, so you will have to handle uppercase and mixed case strings 
	appropriately. 
	
	The score for a word is the product of two components:
	
	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
	 1, or
	 7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
	 and n is the hand length when the word was played
	
	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
	
	word: string
	n: int >= 0
	returns: int >= 0
	"""
    
    

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    print("Current hand: ")
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3) - 1)

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    hand["*"] = 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    word_in_lowercase = word.lower()
    for char in word_in_lowercase:
    	if char in new_hand.keys() and new_hand[char] > 0:
    		new_hand[char] = new_hand[char] - 1
    	else:
    		pass
    return new_hand
    

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_in_lowercase = word.lower()
    hand_copy = hand.copy()
    if "*" in word_in_lowercase:
    	for v in VOWELS:
    		if word_in_lowercase.replace("*", v) in word_list:
    			return True
    		else: 
    			continue
    	print("That is not a valid word. Please choose another word.")
    	return False
    else:
    	if word_in_lowercase not in word_list:
            print("That is not a valid word. Please choose another word.")
            return False
    	else:
    		for char in word_in_lowercase:
    			if char in hand_copy.keys() and hand_copy[char] > 0:
    				hand_copy[char] = hand_copy[char] - 1
    			else:
    				print("Some of the characters used are not included in the hand.")
    				return False
    		return True		

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length_of_hand = 0
    for letter in hand.keys():
    	if letter != "*":
    		length_of_hand += hand[letter]
    	else:
    		pass
    return int(length_of_hand)

    
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    Total_score = 0
    display_hand(hand)
    word = str(input("Enter word, or !! to indicate that you are finished:"))
    while calculate_handlen(hand) != 0:
        if word == "!!":
            print("Total score: " + str(Total_score) + " points.")
            break
        else:    
            if is_valid_word(word, hand, word_list) == True:
                current_score = get_word_score(word, n)
                Total_score += current_score 
                print (word + " earned " + str(current_score) + " points. Total: " + str(Total_score) + " points.") 
                hand = update_hand(hand, word)
            else:
                #is_valid_word(word, hand, word_list, True)
                hand = update_hand(hand, word)
        if calculate_handlen(hand) == 0:
            print("Ran out of letters. Total score: " + str(Total_score) + " points")
            break
        else:
            display_hand(hand)
            word = str(input("Enter word, or !! to indicate that you are finished:"))
    return Total_score 
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    available_letters = VOWELS + CONSONANTS
    hand_replaced = hand.copy()
    if letter not in hand.keys():
    	return hand
    else:
    	num_of_occurence = hand_replaced[letter]
    	del hand_replaced[letter]
    	for char in hand_replaced.keys():
    		available_letters = available_letters.replace(char, "")
    	new_letter = random.choice(available_letters)
    	hand_replaced[new_letter] = num_of_occurence
    	return hand_replaced
    
# Function for performing step 1 in game
def check_substitute_letter_availability( \
		num_of_letter_substitution_used,  \
		hand                              \
	):
    hand_local = hand.copy()
    if num_of_letter_substitution_used == 0:
    	letter_substitution = str(input("Would you like to substitute a letter? Please enter yes or no: "))
    	assert letter_substitution == "yes" or letter_substitution == "no", "Invalid answer. Please enter yes or no."
    	if letter_substitution == "yes":
    		intended_letter = str(input("Which letter would you like to replace: "))
    		hand_local = substitute_hand(hand_local, intended_letter)
    		num_of_letter_substitution_used += 1
    		return num_of_letter_substitution_used, hand_local
    	if letter_substitution == "no":
    		return num_of_letter_substitution_used, hand_local
    else:
    	print("No substitutions available, continuing...")
    	return num_of_letter_substitution_used, hand_local

# Function for performing stage 2 in game
def play_single_round(hand, n):
    hand_local = hand.copy()
    point_for_this_round = 0
    display_hand(hand_local)
    
    while calculate_handlen(hand) != 0:
    	word = str(input("Enter word, or !! to indicate that you are finished: "))
    	# Process word and check if it is exit code "!!"
    	if word == "!!":
    		break
    	else:    
    		if is_valid_word(word, hand_local, word_list) == True:
    			current_point = get_word_score(word, n)
    			point_for_this_round += current_point 
    			print ("[[ " + word + " ]]" + " earned " + str(current_point) + " points. Accumulated points for this round: " + str(point_for_this_round) + " points.") 
    			hand_local = update_hand(hand_local, word)
    		else:
    			hand_local = update_hand(hand_local, word)
    	# Display updated hand
    	display_hand(hand_local)
    	# Decide whether to continue:
    	if calculate_handlen(hand_local) == 0:
    		print("Ran out of letters. Accumulated points for this round: " + str(point_for_this_round) + " points")
    		break
    return point_for_this_round

# Function for performing stage 3 in game
def attempt_retry( \
		num_of_replay_used, \
		hand, \
		point_from_first_try, \
		n):
    if num_of_replay_used == 0:
    	replay_this_hand = str(input("Would you like to replay the hand? Please enter yes or no: "))
    	assert replay_this_hand == "yes" or replay_this_hand == "no", "Invalid answer. Please enter yes or no: "
    	if replay_this_hand == "yes":
    		point_from_second_try = play_single_round(hand, n)
    		num_of_replay_used += 1
    		if point_from_second_try > point_from_first_try:
    			print("You scored higher this time. Your new score is: " + str(point_from_second_try))
    			return point_from_second_try, num_of_replay_used
    		elif point_from_second_try < point_from_first_try:
    			print("You scored lower this time. Your previous score is: " + str(point_from_first_try)) 
    			return point_from_first_try, num_of_replay_used
    		else:
    			print("Your score has remained the same: " + str(point_from_first_try))
    			return point_from_first_try, num_of_replay_used
    	else:
    		return point_from_first_try, num_of_replay_used
    else:
    	return point_from_first_try, num_of_replay_used

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    n = HAND_SIZE
    hand = deal_hand(n)
    num_of_hands = int(input("Enter total number of hands: "))
    num_of_letter_substitution_used = 0
    num_of_replay_used = 0
    total_score   = 0
    current_round = 0
    
    '''
    One round is divided into five stages:
      0. Print helper messages
      1. Check if substitution is available
      2. Play hand for this round
      3. Check if replay is available
      4. Miscellaneous tasks
    '''
    while current_round < num_of_hands:
    	# Stage 0
    	print("===========================\n          ROUND {}".format(current_round + 1))
    	print("Substitution Left: {}\nReplay Left: {}\nTotal Score: {}".format(1 - num_of_letter_substitution_used, 1 - num_of_replay_used, total_score))
    	print("===========================")
    	display_hand(hand)
    	
    	# Stage 1
    	num_of_letter_substitution_used, hand = \
    		check_substitute_letter_availability(num_of_letter_substitution_used, hand)

    	# Stage 2
    	point_from_first_try = play_single_round(hand, n)
    	
    	# Stage 3
    	final_point, num_of_replay_used = attempt_retry(num_of_replay_used, hand, point_from_first_try, n)

    	# Stage 4 
    	total_score += final_point
    	hand = deal_hand(n)
    	current_round += 1

    print("End of Game.")
    return total_score
    
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    #play_hand(hand, word_list)
    Total_score = play_game(word_list)
    print("Your total score is: " + str(Total_score))