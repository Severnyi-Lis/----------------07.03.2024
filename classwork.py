
tovars = {
 'milk':'молоко',
 'bread':'хлеб',
 'butter':'масло'
}
 
cena = {
    'bread': 50,
    'milk': 88,
    'butter': 127,
}
for lll in tovars:
 print(tovars[lll],cena[lll])
res = 0
for fff in cena:
 res+=cena[fff]
print('Итого',res,'рублей')


new_good = input('Какой товар добавить? ')
while new_good!='все!':
 price = int(input('Сколько он стоит? '))
 tovars[new_good] = price
 for g in tovars:
  print(g, tovars[g])

