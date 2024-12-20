vowels = ['a','e','i','o','u']
digits = ['0','1','2','3','4','5','6','7','8','9']
punctuations = [",",";",'.','?','!',]
character = input("Please enter a character: ")
if character.lower() in vowels:
    print(f"The character '{character}' is a vowel.")
elif character in digits:
    print(f"The character '{character}' is a digit.")
elif character in punctuations:
    print(f"The character '{character}' is a punctuation")
elif character.lower().isalpha:
    print(f"The character '{character}' is a consonent")
