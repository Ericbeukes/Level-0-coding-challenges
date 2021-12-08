def find_vowels(phrase):
  print("Vowels:")
  sentence = (phrase).lower()
  for vowel in 'aeiou':
    if vowel in sentence:
      print(vowel, end="")

find_vowels("Umuzi")