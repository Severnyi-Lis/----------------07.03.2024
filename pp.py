Word = { 
} 
print  ('Словарь пустой ') 
new_word = input('Какое слово добавить')
translate = input('Перевод')
Word[new_word] = translate
for w in Word:
    while new_word == "Все":
       
       print(w, Word[w])