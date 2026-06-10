#Product Review Analyzer Problem
review = "This product is excellent excellent excellent and very useful"

# Convert review into a list of words
words = review.split()

# 1. Count total words
print("Total Words:", len(words))

# 2. Create dictionary containing word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")
for word, count in frequency.items():
    print(word, "->", count)

# 3. Find most frequently used word
most_frequent = max(frequency, key=frequency.get)
print("\nMost Frequent Word:", most_frequent)

# 4. Find all words appearing only once
once_words = []

for word, count in frequency.items():
    if count == 1:
        once_words.append(word)

print("Words Appearing Once:", once_words)

# 5. Count words having more than 5 characters
count_long = 0

for word in words:
    if len(word) > 5:
        count_long += 1

print("Words Having More Than 5 Characters:", count_long)

# 6. Display words in reverse order
print("Words in Reverse Order:", words[::-1])

# 7. Create a list of unique words
unique_words = list(frequency.keys())

print("Unique Words:", unique_words)