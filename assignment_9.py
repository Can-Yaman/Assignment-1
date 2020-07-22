sentence = input("Type your sentence here: ")
letters = set(sentence)
result = {}
for i in letters:
    result[i] = sentence.count(i)
print( "Numbers of letters/chars in your sentences:")
print(result)