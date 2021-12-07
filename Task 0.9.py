sentence = ("Umuzi").lower()

def find_vowels():
    for vowel in 'aeiou':
     if vowel in sentence:
       print(vowel, end="")

print("Vowels:")
find_vowels()