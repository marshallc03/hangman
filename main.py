from replit import clear
import random
import hangman_art
import hangman_words

print(hangman_art.logo + "\n\n")
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

#Print statement below for testing code: 
#print(f"The solution is {chosen_word}.")

display = []
for _ in range(word_length):
  display.append("_")

print(hangman_art.stages[lives])
print(display)

end_of_game = False

while not end_of_game:
  guess = input("\nGuess a letter: ").lower()

  clear()

  if guess in display:
    print(f"You already guessed {guess}. Choose another letter.")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = guess
  
  if guess not in chosen_word:
    lives -= 1
    print(f"There is no {guess} in this word.")
    if lives == 0:
      end_of_game = True
      print(f"You lose. The word was: {chosen_word}.")
    else:
      print(f"You have {lives} chances left.")
  
  print(display)

  if "_" not in display:
    end_of_game = True
    print("You won!")

  print(hangman_art.stages[lives])
