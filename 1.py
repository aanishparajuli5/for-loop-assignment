text = input("Enter a word or sentence: ")

vowels = {'a', 'e', 'i', 'o', 'u'}
found_vowels = set()

for ch in text.lower():
    if ch in vowels:
        found_vowels.add(ch)

print("Unique vowels found:", found_vowels)
print("Total number of unique vowels:", len(found_vowels))