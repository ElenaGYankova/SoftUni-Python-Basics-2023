characters = input()

for symbol in characters:
    print(symbol)

# some_text = input()
# for index in range(0, len(some_text)):
#    print(some_text[index])

''' можем да достъпим 2та буква, като:
some_text = 'text'
print(some_text[1]) или в обратен ред:
print(some_text[-3])
обратното броене започва от последната буква като тя е -1
'''

'''
some_text = 'te xt'
for index, symbol in enumerate(some_text):
    print(f"Index = {index}, Symbol = {symbol}")
'''