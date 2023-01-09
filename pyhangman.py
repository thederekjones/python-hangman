import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

print(hangman_art.logo)
#Testing code
print(f'The solution is {chosen_word}.')

display = []

for letter in chosen_word:
    display.append("_")

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    if lives == 6:
        print(hangman_art.stages[6])
    elif lives == 5:
        print(hangman_art.stages[5])
    elif lives == 4:
        print(hangman_art.stages[4])
    elif lives == 3:
        print(hangman_art.stages[3])
    elif lives == 2:
        print(hangman_art.stages[2])
    elif lives == 1:
        print(hangman_art.stages[1])
    elif lives == 0:
        print(hangman_art.stages[0])