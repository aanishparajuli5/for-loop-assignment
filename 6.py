sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = {}

for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1

for word in sorted(word_count):
    print(word, ":", word_count[word])