print('Welcome to the tip calculator.')
bill = float(input('Whats was the total bill? '))
people = int(input('How many people to split the bill? '))
percentage = int(input('What percentage Tip would you like to give? 10, 12, or 15? '))

if percentage == 10:
    value = (bill * 1.10) / people
    print(f'Each Person should pay: {value:.2f}')
elif percentage == 12:
    value = (bill * 1.12) / people
    print(f'Each Person should pay: {value:.2f}')
elif percentage == 15:
    value = (bill * 1.15) / people
    print(f'Each Person should pay: {value:.2f}')
else: 
    print('Error')