import sys
from collections import Counter

text_file = open(sys.argv[1])
text_file = text_file.read()
text_file = text_file.lower()

for c in text_file:
    if c in "?.!/;:,'\"_":
        text_file = text_file.replace(c, "")

words = text_file.split()

word_count = Counter(words)

for word, count in sorted(word_count.items()):
    print word, count


# word_count = {}

# for line in text_file:
#     line = line.rstrip()
#     line = line.lower()
#     for c in line:
#         if c in "?.!/;:,'\"_":
#             line = line.replace(c, "")
#     words = line.split()
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1


# for word, count in word_count.items():
#     print word, count
