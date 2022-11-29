from random import randint

jeden = 0
dwa = 0
trzy = 0
cztery = 0
piec = 0
szesc = 0

ile = input('Podaj ilość losowań: ')
i = 0
while i < int(ile):
    los = randint(1, 6)
    if los == 1:
        jeden += 1
    elif los == 2:
        dwa += 1
    elif los == 3:
        trzy += 1
    elif los == 4:
        cztery += 1
    elif los == 5:
        piec += 1
    elif los == 6:
        szesc += 1
    i += 1



w1 = round((jeden / i)*100, 2)
w2 = round((dwa / i)*100, 2)
w3 = round((trzy / i)*100, 2)
w4 = round((cztery / i)*100, 2)
w5 = round((piec / i)*100, 2)
w6 = round((szesc / i)*100, 2)


print(f'Ilość 1: {w1}%')
print(f'Ilość 2: {w2}%')
print(f'Ilość 3: {w3}%')
print(f'Ilość 4: {w4}%')
print(f'Ilość 5: {w5}%')
print(f'Ilość 6: {w6}%')