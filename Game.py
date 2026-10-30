import random

WORDS = ["python", "planet", "guitar", "water", "bridge"]
MAX_WRONG = 6

def play():
   
    word = random.choice(WORDS)
    guessed = []   
    wrong = 0     
    print("Welcome to Hangman!")

    while wrong < MAX_WRONG:
  
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "
        print("\nWord:", display)

        if "_" not in display:
            print("You won! The word was:", word)
            return

        print("Wrong guesses left:", MAX_WRONG - wrong)
        print("Letters tried:", ", ".join(sorted(guessed)))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already tried that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            wrong += 1
            print("Nope, that letter is not in the word.")

    print("\nGame over! The word was:", word)

play()
