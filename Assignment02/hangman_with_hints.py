# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("\tLoading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("\t  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_character_list = list(secret_word)
    for char in secret_word_character_list:
    	if char not in letters_guessed:
    		return False
    	else:
    		pass
    return True






def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    hint_string = ""
    secret_word_character_list = list(secret_word)
    for char in secret_word_character_list:
    	if char in letters_guessed:
    		hint_string += str(char)
    	else:
    		hint_string += "_ "
    return(hint_string)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_of_all_letters = list(string.ascii_lowercase)
    for char in letters_guessed:
    	list_of_all_letters.remove(char)
    available_string = ''.join(list_of_all_letters)
    return available_string

    
def print_turn_helper_message(secret_word, guesses, letters_guessed):
	print("\tI am thinking of a word that is " + str(len(secret_word)) + " letters long.")
	print("\tYou have " + str(guesses) + " guesses left.")
	print("\tAvailable letters: " + get_available_letters(letters_guessed))
	print("\tYou can enter * for hints.")

def total_score (guesses, secret_word):
	unique_letters = list(set(secret_word))
	return guesses * len(unique_letters)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("\tWelcome to the game Hangman!")
    guesses = 6
    warnings = 3
    letters_guessed = []
    vowel_list = ["a","e","i","o","u"]
    while guesses > 0 and get_guessed_word(secret_word, letters_guessed) != secret_word:
    	#step 1: print message
    	print_turn_helper_message(secret_word = secret_word, guesses = guesses, letters_guessed = letters_guessed)
		
		#step 2: make sure input is a valid letter
    	guess_input = input("\tPlease guess a letter: ")
    	if str.lower(guess_input) not in string.ascii_lowercase:
    		warnings = warnings - 1
    		print("\tOops! That is not a valid letter.") 
    		if warnings > -1:
    			print("\tYou have " + str(warnings) + " warnings left")
    		print("\t\t" + get_guessed_word(secret_word, letters_guessed))
    		if warnings <= -1:
    			guesses = guesses - 1
    		continue
    	if str.lower(guess_input) in letters_guessed:
    		warnings = warnings - 1
    		print("\tOops! You've already guessed that letter.")
    		if warnings > -1:
    			print("\tYou have " + str(warnings) + " warnings left")
    		print("\t\t" + get_guessed_word(secret_word, letters_guessed))
    		if warnings <= -1:
    			guesses = guesses - 1
    		continue
    	letters_guessed.append(guess_input)
    	#step 3: handling guessed letters
    	if guess_input not in list(secret_word):
    		if guess_input in vowel_list:
    			guesses = guesses - 2
    		else:
    			guesses = guesses - 1
    		print("\tOops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
    	else:
    		print("\tGood guess!" + get_guessed_word(secret_word, letters_guessed))
    
    if get_guessed_word(secret_word, letters_guessed) == secret_word:
    	print("\tCongratulations, you won!")
    	print("\tYour total score for this game is: " + str(total_score(guesses,secret_word)))
    else:
    	print("\tSorry, you ran out of guesses. The word was " + secret_word)
		





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_in_list = list(my_word.replace(" ",""))
    other_word_list = list(other_word)
    n = len(my_word_in_list)
    if n == len(other_word_list):
        for index in range(n):
            if my_word_in_list[index] != "_":
                if my_word_in_list[index] == other_word_list[index]:
                    continue
                else:
                    return False
        return True
    else:
        return False






def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    number_of_correct_matches = 0
    print("\tPossible word matches are: ")
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            print("\t\t" + other_word)
            number_of_correct_matches += 1
        else:
            pass
    if number_of_correct_matches == 0:
        print("\tNo matches found.")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("\tWelcome to the game Hangman!")
    guesses = 6
    warnings = 3
    letters_guessed = []
    vowel_list = ["a","e","i","o","u"]
    while guesses > 0 and get_guessed_word(secret_word, letters_guessed) != secret_word:
        #step 1: print message
        print_turn_helper_message(secret_word = secret_word, guesses = guesses, letters_guessed = letters_guessed)
        
        #step 2: make sure input is a valid letter
        guess_input = input("\tPlease guess a letter: ")
        if str.lower(guess_input) not in string.ascii_lowercase and str.lower(guess_input) != "*":
            warnings = warnings - 1
            print("\tOops! That is not a valid letter.") 
            if warnings > -1:
                print("\tYou have " + str(warnings) + " warnings left")
            print("\t\t" + get_guessed_word(secret_word, letters_guessed))
            if warnings <= -1:
                guesses = guesses - 1
            continue
        if str.lower(guess_input) in letters_guessed:
            warnings = warnings - 1
            print("\tOops! You've already guessed that letter.")
            if warnings > -1:
                print("\tYou have " + str(warnings) + " warnings left")
            print("\t\t" + get_guessed_word(secret_word, letters_guessed))
            if warnings <= -1:
                guesses = guesses - 1
            continue
        if str.lower(guess_input) == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        letters_guessed.append(guess_input)
        #step 3: handling guessed letters
        if guess_input not in list(secret_word):
            if guess_input in vowel_list:
                guesses = guesses - 2
            else:
                guesses = guesses - 1
            print("\tOops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
        else:
            print("\tGood guess!" + get_guessed_word(secret_word, letters_guessed))
    
    if get_guessed_word(secret_word, letters_guessed) == secret_word:
        print("\tCongratulations, you won!")
        print("\tYour total score for this game is: " + str(total_score(guesses,secret_word)))
    else:
        print("\tSorry, you ran out of guesses. The word was " + secret_word)
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
