print('Welcome to the rollercoaster')
height = int(input('What is your height in cm? '))
if height >= 120:
    print('You can Ride the rollercoster!')
    age = int(input('What is your age? '))
    photo = int(input('Do you want a photo? \n [1]Yes [2]No:  '))
    if age <12:
        if photo == 1:
            print('You have to pay $8.')
        else:
            print('You have to pay $5.')
    elif age <=18:
        if photo == 1:
            print('You have to pay $10.')
        else:
            print('You have to pay $7.')
    else:
        if photo == 1:
            print('You have to pay $15.')
        else:
            print('You have to pay $12.')
else: print('Sorry, you have to grow taller before you can ride.')