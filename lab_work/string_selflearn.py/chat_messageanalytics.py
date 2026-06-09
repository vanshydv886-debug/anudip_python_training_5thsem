#program for chat meassage analytics 
message = "python is awesome and python is easy to underdtand"

print("Message:", message)

# 1. Total Characters
print("Total Characters:", len(message))

# Convert message into list of words
words = message.split()

# 2. Total Words
print("Total Words:", len(words))

# 3. Longest Word
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)

# 4. Shortest Word
shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word:", shortest)

# 5. Count occurrences of Python
count_python = words.count("Python")

print("Occurrences of Python:", count_python)

# 6. Words having more than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters:", long_words)

# 7. Words starting with a vowel
print("Words Starting With a Vowel:")

for word in words:
    if word[0].lower() in "aeiou":
        print(word)

# 8. Count vowels and consonants
vowels = 0
consonants = 0

for ch in message.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)