dictionary = {}
unique_words = set()

turns = int(input("How many operations do you want to perform? "))

for _ in range(turns):
    print("\nMenu")
    print("1. Add word")
    print("2. Display all words")
    print("3. Remove word")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        word = input("Enter word: ").lower()
        meaning = input("Enter meaning: ")

        if word in dictionary:
            print("Word already exists.")
        else:
            dictionary[word] = meaning
            unique_words.add(word)
            print("Word added successfully.")

    elif choice == '2':
        for word in sorted(dictionary):
            print(f"Word: {word}, Meaning: {dictionary[word]}")

    elif choice == '3':
        word = input("Enter word to remove: ").lower()
        if word in dictionary:
            dictionary.pop(word)
            unique_words.discard(word)
            print("Word removed.")
        else:
            print("Word not found.")

    elif choice == '4':
        print("Exit")
        break

    else:
        print("Invalid choice")

print("\nFinal set of unique words:", unique_words)