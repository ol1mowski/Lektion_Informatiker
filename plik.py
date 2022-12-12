from random import randint

jeden = 0
dwa = 0
trzy = 0
cztery = 0
piec = 0
szesc = 0

ile = int(input('Podaj ilość losowań: '))
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

w1 = jeden
w2 = dwa
w3 = trzy
w4 = cztery
w5 = piec
w6 = szesc



sw1 = round((jeden / ile)*100, 2)
sw2 = round((dwa / ile)*100, 2)
sw3 = round((trzy / ile)*100, 2)
sw4 = round((cztery / ile)*100, 2)
sw5 = round((piec / ile)*100, 2)
sw6 = round((szesc / ile)*100, 2)


print(f'Ilość 1: {sw1}%')
print(f'Ilość 2: {sw2}%')
print(f'Ilość 3: {sw3}%')
print(f'Ilość 4: {sw4}%')
print(f'Ilość 5: {sw5}%')
print(f'Ilość 6: {sw6}%')

if w1 > w2 and w1 > w3 and w1 > w4 and w1 > w5 and w1 > w6:
    print('Najczęściej wypadłała 1')
    odch = ((6 / ile) - w1) / 100
    print(f'Odchyła od średniej wynosi: {odch}%')
elif w2 > w1 and w2 > w3 and w2 > w4 and w2 > w5 and w2 > w6:
    print('Najczęściej wypadłała 2')
    odch = ((6 / ile) - w2) / 100
    print(f'Odchyła od średniej wynosi: {odch}%')
elif w3 > w1 and w3 > w2 and w3 > w4 and w3 > w5 and w3 > w6:
    print('Najczęściej wypadłała 3')
    odch = ((6 / ile) - w3) / 100
    print(f'Odchyła od średniej wynosi: {odch}%')
elif w4 > w1 and w4 > w2 and w4 > w3 and w4 > w5 and w4 > w6:
    print('Najczęściej wypadłała 4')
    odch = ((6 / ile) - w4) / 100
    print(f'Odchyła od średniej wynosi: {odch}%')
elif w5 > w1 and w5 > w2 and w5 > w3 and w5 > w4 and w5 > w6:
    print('Najczęściej wypadłała 5')
    odch = ((6 / ile) - w5) / 100
    print(f'Odchyła od średniej wynosi: {odch}%')
elif w6 > w1 and w6 > w2 and w6 > w3 and w6 > w4 and w6 > w5:
    print('Najczęściej wypadłała 6')
    odch = ((6 / ile) - w6) / 100
    print(f'Odchyła od średniej wynosi: {odch}%')
else:
    print('Jakieś liczby wypadały tak samo często! Sprawdź tabelkę powyżej')