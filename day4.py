from random import randint

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

while True:
    player = int(input(f'What do you choose? \nType [0] for Rock\n {rock}, [1] for Paper\n {paper}, or [2] for Scissors.\n {scissors}'))
    choice = randint(1,3)
    if player >= 3 or player < 0:
        print('You typed an invalid number, you LOSE!')
    elif player == 0 and choice == 2:
        print(f' YOU WIN ')
    elif player == 0 and choice == 2:
        print(f' YOU LOSE ')
    elif player > choice:
        print('YOU win')
    elif choice > player:
        print('You lose')
    elif choice == player:
        print('ITS A DRAW')
    keep_going = int(input('CONTINUE ?\n [1] Yes, [2]No'))
    if keep_going == 1:
        continue
    elif keep_going == 2:
        break
    else:
        print('Choose 1 or 2')