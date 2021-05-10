words = 1
chars = 0

things = input('Write About Yourself Here: ')

for i in things:
    chars += 1
    if(i == ' '):
        words += 1

print('chars: ' + str(chars) + '      '  + 'words: ' + str(words))
