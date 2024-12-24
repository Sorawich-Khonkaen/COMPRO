import time
Amount = int(input('Enter the amount you want to deposit: '))
years = int(input('Enter the number of years: '))
mon = int(input('Select daily deposit, press 1, monthly deposit, press 2: '))

if mon == 1:
    money = Amount / (years * 365)
    print(('Amount of money to be collected daily'),money)
    
elif mon == 2:
    money = Amount / (years * 12)
    print(('Amount to be collected monthly'),money)