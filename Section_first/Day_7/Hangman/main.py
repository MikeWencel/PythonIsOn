import random
import hangman_words
import hangman_draw
import os



display = []
end_of_game = False
#Lista słów do odgadnięcia
#Losowanie słowa
random_word = random.choice(hangman_words.word_list)
#print(random_word)
lives = 6
is_letter = False
for x in random_word:
    display += "_"
    
print(display)




while not end_of_game:
    
    guess = input("Podaj literę: ")
     
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter          
        
    if "_" not in display:
        print("You win")
        print("Game Over")
        end_of_game = True


            
    if guess not in random_word:
        lives -= 1
        print(f"You've got {lives} more lives")
        if lives == 0:
            print("You lost - Game Over!")
            print(f"Random word: {random_word}")
            end_of_game = True        
        
    print(f"{' '.join(display)}")
    print(hangman_draw.stages[lives]) 

#Przypadek gdy trafiona litera - wyświetlenie
