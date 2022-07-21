anything = input("type any word you want: ").lower()
vowels = ["y", 'i', 'e', "o", "u", "a", "I", "O", "E", "U", "A", "Y"]

i = 0

while i < len(anything):
    if anything[i] in vowels:
        anything = anything.replace(anything[i], "")
        continue

    i += 1
print("\nWithout Vowels =", anything)


