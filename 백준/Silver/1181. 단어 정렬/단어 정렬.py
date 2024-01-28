num_words = int(input())
input_words = set()

for _ in range(num_words):
    word = input()
    input_words.add(word)

sorted_words = sorted(input_words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
