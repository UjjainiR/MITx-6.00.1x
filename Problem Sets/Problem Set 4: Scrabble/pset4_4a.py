# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

# WORDLIST_FILENAME = "words.txt"
WORDLIST_FILENAME = "D:/MITx 6.00.1x and 6.00.2x/MIT 6.00.1x/Problem Sets/Problem Set 4/New/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
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


# Problem 1: Scoring a word
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    return sum(SCRABBLE_LETTER_VALUES[c] for c in word)*len(word) + 50*(n==len(word))  


# For Problem 2, Make sure you understand how this function works and what it does!
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

# Problem 2: Update a hand by removing letters
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    return {c: (hand[c] - word.count(c)) for c in hand}


# Problem 3: Test word validity
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    return word in wordList and all(hand.get(c, 0) >= word.count(c) for c in word)


# Problem 4: Playing a Hand
def calculateHandlen(hand):
    return sum(hand.values())

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points) 
    """
    total_score = word_score = 0
    hand_length = calculateHandlen(hand)
    while hand_length > 0:
        print("Current Hand: ", end = "")
        displayHand(hand)
        word = input("Enter word, or a '.' to indicate that you are finished: ")
        if word == ".":
            break
        elif not isValidWord(word, hand, wordList):
            print("Invalid word, please try again.\n")  
        else:
            word_score = getWordScore(word, n)
            total_score += word_score
            print(word, "earned", word_score, "points. Total:", total_score, "points\n")
            hand = updateHand(hand, word)
            hand_length = calculateHandlen(hand)         
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if hand_length > 0:
        print("Goodbye! Total score:", total_score, "points.\n")            
    else:
        print("Run out of letters. Total score:", total_score, "points.\n")


# Problem 5: Playing a Game 
def playGame(wordList, hand=None):  
    choice = input('Enter n for a new hand, r to replay, e to end: ')
    hand = dealHand(HAND_SIZE) if choice == 'n' else hand
    playHand(hand, wordList, HAND_SIZE) if choice == 'n' or choice == 'r' and hand else 0
    print('Please play a new hand first!\n' if choice == 'r' and not hand else
          'Invalid command.\n' if choice not in 'nre' else '', end='')
    return None if choice == 'e' else playGame(wordList, hand)



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)
    playGame(wordList)
