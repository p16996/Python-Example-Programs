word = ' '
sentence = ' '
print("please enter some words.")
print("Include (.) when you are done")
while '.' not in word:
    word = raw_input('next word: ')
    sentence = word+''+sentence
print()
print('you said:')
print(sentence)
