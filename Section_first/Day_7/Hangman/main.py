import random
#Step 1 

word_list = ["masło", "chleb", "słońce"]

#random_num = random.randint(0,2)
#chosen_word = word_list[random_num]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
display = []
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

num = 0
for el in chosen_word:
    num += 1

for x in range(num):
    display += "_"
print (display)

#Guessing
guess_letter = input("Choose the letter ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess_letter:
        display[position] = letter
        
print(display)

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
