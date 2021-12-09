def vowel(text):
  vowels = 'aeiuo' 
  res = set([letter for letter in text.lower() if letter in vowels])
  print("Vowels: " + ", ".join(res))
    
vowel("Umuzi")
