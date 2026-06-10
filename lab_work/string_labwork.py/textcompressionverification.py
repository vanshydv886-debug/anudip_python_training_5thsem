# Original text
text = "AAABBBCCCDDDAAA"

# Dictionary for frequencies
frequency = {}

for ch in text:

    if ch in frequency:
        frequency[ch] += 1

    else:
        frequency[ch] = 1

# Display frequencies
print("Character Frequencies:")

for key, value in frequency.items():
    print(key, "->", value)

# Unique characters
unique = list(frequency.keys())

print("Unique Characters:", unique)

# Most frequent character
max_char = ""
max_count = 0

for key, value in frequency.items():

    if value > max_count:
        max_count = value
        max_char = key

print("Most Frequent Character:", max_char)

# Create compressed output
compressed = ""

count = 1

for i in range(len(text) - 1):

    if text[i] == text[i + 1]:

        count += 1

    else:

        compressed += text[i] + str(count)

        count = 1

compressed += text[-1] + str(count)

print("Compressed Output:", compressed)

# Compression ratio
original_length = len(text)
compressed_length = len(compressed)

ratio = (compressed_length / original_length) * 100

print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", round(ratio, 2), "%")