import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("rock, scissors, paper")
choose = input("Choose somethin and win against computer! rock, scissors, paper ")

lower_choose = choose.lower()

if lower_choose == "rock":
    print(rock)
elif lower_choose =="scissors":
    print(scissors)
elif lower_choose =="paper":
    print(paper)


comp_choice = random.randint(1,3)

if comp_choice == 1:
    print(rock)
elif comp_choice == 2:
    print(scissors)
elif comp_choice == 3:
    print(paper)

if lower_choose == "rock" and comp_choice == 2:
    print("You win!")
elif lower_choose == "rock" and comp_choice == 1:
    print("draw")
elif lower_choose == "rock" and comp_choice == 3:
    print("You lose!")

if lower_choose == "scissors" and comp_choice == 3:
    print("You win!")
elif lower_choose == "scissors" and comp_choice == 2:
    print("draw")
elif lower_choose == "scissors" and comp_choice == 1:
    print("You lose!")

if lower_choose == "paper" and comp_choice == 1:
    print("You win!")
elif lower_choose == "paper" and comp_choice == 3:
    print("draw")
elif lower_choose == "paper" and comp_choice == 2:
    print("You lose!")    