import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Testing code
print(f'The solution is {chosen_word}.')

display = []

for letter in chosen_word:
  display.append("_")

while "_" in display:
  guess = input("Guess a letter: ").lower()
  for index in range(len(chosen_word)):
    if chosen_word[index] == guess:
      display[index] = guess
  print(f"{' '.join(display)}")

if "_" not in display:
  print("You win.")