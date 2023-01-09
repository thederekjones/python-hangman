import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#Testing code
print(f'The solution is {chosen_word}.')

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# Create an empty List called display.
display = []

# For each letter in the chosen_word, add a "_" to 'display'.
for letter in chosen_word:
  display.append("_")
  
# Loop through each position in the chosen_word; If the letter at that position
# matches 'guess' then reveal that letter in the display at that position.
for index in range(len(chosen_word)):
  if chosen_word[index] == guess:
    display[index] = guess

print(display)