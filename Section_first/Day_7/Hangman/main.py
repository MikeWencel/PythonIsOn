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
        print("Zwycięstwo")
        print("Koniec Gry")
        end_of_game = True


            
    if guess not in random_word:
        lives -= 1
        print(f"Pozostało {lives} żyć")
        if lives == 0:
            print("Przegrana - koniec gry!")
            print(f"Losowe słowo {random_word}")
            end_of_game = True        
        
    print(f"{' '.join(display)}")
    print(hangman_draw.stages[lives]) 


