import random
from words import wordlist

print("HANGMAN GAME!")

def HM():

    word = random.choice(wordlist).upper()
    wc = "_" * len(word)

    tries = 7
    guessed_letters = []
    guessed_words = []
    guessed = False
    print(wc)




    while not guessed  and tries > 0:
        guess = input("Guess a letter or a word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter",guess,".")

            elif guess not in word:

                guessed_letters.append(guess)
                print("this letter is not in the word")
                tries -= 1

            else:

                guessed_letters.append(guess)
                print("Good guess! The letter ",guess," is in the word.")
                wordal = list(wc)
                indices = [ i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    wordal[index] = guess
                wc = "".join(wordal)
                if "_" not in wc:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():

            if guess in guessed_words:
                print("You have already guessed this word")

            elif guess != word:
                print(guess,"is not the word")
                tries -= 1
                guessed_words.append(guess)

            else:
                guessed = True
                wc = word#

        elif guess.isalpha():
            if guess != word:
                print(guess, "is not the word")
                tries -= 1

        print(wc)
        print(hangman(tries))
        print()

    if guessed:
        print("You have guessed the word!")
    else:
        print("Unlucky you have ran out of tries :(, the word was",word.lower())

def hangman(tries):
    stages = ["""

                    ----------
                    |        |
                    |        |
                    |        
                    |       
                    |        
                    |       
                    |

                """,
                """

                    ----------
                    |        |
                    |        |
                    |        O
                    |      
                    |        
                    |       
                    |

                """,
                """

                    ----------
                    |        |
                    |        |
                    |        O
                    |        | 
                    |        
                    |       
                    |
                """,
                """

                    ----------
                    |        |
                    |        |
                    |        O
                    |      \ | 
                    |        
                    |       
                    |
                """,
                """

                    ----------
                    |        |
                    |        |
                    |        O
                    |      \ | /
                    |        
                    |       
                    |
                """,
                """

                    ----------
                    |        |
                    |        |
                    |        O
                    |      \ | /
                    |        |
                    |       
                    |
                """,
                """

                    ----------
                    |        |
                    |        |
                    |        O
                    |      \ | /
                    |        |
                    |       /
                    |
                """,
                """

                    ----------
                    |        |
                    |        |
                    |        O
                    |      \ | /
                    |        |
                    |       / \ 
                    |
                """


    ]
    return stages[tries]

HM()

while input("Would you like to play again? (y/n): ") == "y":
    HM()