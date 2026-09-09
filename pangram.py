text = input("Enter a string:")
letters = set(text.lower())
alphabet = set("abcdefghijklmnopqrstuvwxyz")
if alphabet.issubset(letters):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
