sentence = input('Enter your word or sentence: ').lower()
print("Vowels:")
for vowel in 'aeiou':
     if vowel in sentence:
       print(vowel, end="")