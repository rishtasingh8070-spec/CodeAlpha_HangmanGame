import random
# 1. Predefined list of 5 words
words = ["python", "coding", "intern", "program", "laptop"]

#  To Select a random word from the list
chosen_word = random.choice(words)

# Create a list of underscores to represent the hidden letters
display = ["_"] * len(chosen_word)

# Game configuration
max_incorrect_guesses = 5
incorrect_guesses = 0
guessed_letters = []

print("Welcome to Hangman!")
print("Try to guess the secret word letter by letter.")

# 2. Main game loop
while "_" in display and incorrect_guesses < max_incorrect_guesses:
    print(f"\nWord to guess: {' '.join(display)}")
    print(f"Guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    # Get user input
    guess = input("Guess a letter: ").lower().strip()
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue
        
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue
        
    # Add to guessed list
    guessed_letters.append(guess)
    
    # 3. Check if the guess is in the chosen word
    if guess in chosen_word:
        print(f"Good job! '{guess}' is in the word.")
        # Update the display list with the correctly guessed letter
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        incorrect_guesses += 1

# 4. Game over check
if "_" not in display:
    print(f"\nCongratulations! You won! The word was: {chosen_word}")
else:
    print(f"\nGame Over! You ran out of guesses. The word was: {chosen_word}")