# This is a project to create a hangman game. The user will have to guess the word by guessing the letters. The user will have a limited number of guesses. If the user guesses the word before running out of guesses, they win. 
# If they run out of guesses, they lose.
import random

# Pictures for visual game. These appear as you guess  an incorrect letter
HANGMANPICS = [r'''   
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print('''
     _________WELCOME TO THE HANGMAN GAME. SAVE A LIFE!!!_______
''')

# random choosing of word from a wordlist
random_words = ["banana", "apple", "arda", "guler", "abdullah", "unicorn","ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat",
    "clam", "cobra", "cougar", "coyote", "crow", "deer", "dog", "donkey",
    "duck", "eagle", "ferret", "fox", "frog", "goat", "goose", "hawk",
    "lion", "lizard", "llama", "mole", "monkey", "moose", "mouse", "mule",
    "newt", "otter", "owl", "panda", "parrot", "pigeon", "python", "rabbit",
    "ram", "rat", "raven", "rhino", "salmon", "seal", "shark", "sheep",
    "skunk", "sloth", "snake", "spider", "stork", "swan", "tiger", "toad",
    "trout", "turkey", "turtle", "weasel", "whale", "wolf", "wombat", "zebra"]
word_chosen = random.choice(random_words)

# asking user to guess the letter


place_holder = ""
l_w = len(word_chosen)

print("-THE WORD HAS BEEN CHOOSEN-")

for i in range(l_w):
    place_holder += "_ "
    
print(place_holder)



correct =[]
lifes = 6 # to follow incorrect guesses
    
game_over = False
i = 0 
while not game_over :  
    display = ""
  
    
    guess_letter = input("Guess letter: ").lower() 
    
    
    if guess_letter in correct:
        print("**TRY ANOTHER : ALREDAY GUESSED**") #if guessed try another
    for w in word_chosen:

        if w == guess_letter:
            display += w 
            correct.append(guess_letter)
            
        elif w in correct:
            display += w
                 
        else:
            display += "_"
    
    
    print(display)      
    
    if guess_letter in correct:
        print(HANGMANPICS[i])
        
    elif guess_letter not in correct:    
        
        lifes -= 1
        i += 1
        print(HANGMANPICS[i])
        if lifes == 0:
            print("""
                ******************
                   YOU LOSE 
                ******************
                """)
            game_over = True
        
        
   
        
    
    if "_" not in display:
        game_over=True
        print("""
            ******************
                YOU WIN     
            ******************
            """)
        
        

            
            
        
        
        
    


