print(""                                           )
print(""                                           )
print("       _V_"                        )
print("       @.@"                        )
print("      (\_/)"                       )
print("       m m"                        )
print(""                                           )
print(          " _     _         _ "              )
print(          "| |   (_)       | |"              )
print(          "| |__  _ _ __ __| |"              )
print(          "| '_ \| | '__/ _` |"              )
print(          "| |_) | | | | (_| |"              )
print(          "|_.__/|_|_|  \__,_|"              )
print(                                             )
print(                                             )

      




print("Welcome to bird adventures!")
print("Help bird excape the house!")

start = input("You fall sleep, and few minutes later you open your eyes and realised that you are a bird! This must be a dream! You need to figure out how to escape from this house! and also.. dream!!! In front of you there are open white doors, one the left it's window, on the right is a mouse hall. What you'll choose. Type Doors, Hole or Window ")
start_lower = start.lower()

if start_lower == "doors":
    print("********************************")
    middle = input("Happy that you still live, you can't land! cause there is angry Shih-Tzu over there. You have to choose left (bedroom) or right (kitchen), type it! " )
    print("********************************")
    middle_lower = middle.lower()
    if middle_lower == "left":
        print("GAME OVER, angry Shih Tzu jump on the bed! and eat you!, you'll be a poop! :(")
    elif middle_lower == "right":
        print("********************************")
        print("You land on the big flower, shih tzu is on the carpet! But it's start to jump and she'll catch you! In few seconds angry shih tzu will overturn this big flower!")
        print("********************************")
        end = input("You must choose balcony or garden! Quick!!! type: balcony or garden ")
        end_lower = end.lower()
        if end_lower == "balcony":
            print("********************************")
            print("You win it was a dream!! :) You're free, you can wake up!")
            print("********************************")
        elif end_lower == "garden":
            print("********************************")
            print("Game Over, a lot of kids, you know what happend!")
elif start_lower == "hole":
    print("GAME OVER, you've been eaten by RAT! Oh no this is LIMBO, you opened your eyes, and you are a RAT now!")
elif start_lower == "window":
    print("GAME OVE you smashed in to the glass! Oh no you're a SNAIL!!")







