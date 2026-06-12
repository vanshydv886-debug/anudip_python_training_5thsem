#program for Chat Message Analytics Dashboard 
from collections import Counter

messages = [
    "Hello how are you",
    "I am doing great today",
    "Python programming is fun",
    "Let's meet tomorrow",
    "Good morning everyone",
    "Happy birthday to you",
    "Have a nice day",
    "Learning Python is interesting",
    "Please send the report",
    "Thank you very much",
    "Welcome to the group",
    "This project is amazing",
    "Keep working hard",
    "Success comes with effort",
    "Practice makes perfect",
    "Enjoy your vacation",
    "The weather is pleasant",
    "I like reading books",
    "Coding improves problem solving",
    "Stay positive and motivated"
]

all_words = []
total_words = 0

longest_message = max(messages, key=len)
shortest_message = min(messages, key=len)

for msg in messages:
    print("\nMessage:", msg)

    words = msg.split()
    all_words.extend(words)

    word_count = len(words)
    total_words += word_count

    char_count = len(msg)

    vowels = 0
    consonants = 0

    for ch in msg.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    freq = Counter(words)

    repeated_words = [word for word, count in freq.items() if count > 1]

    vowel_words = [word for word in words
                   if word[0].lower() in "aeiou"]

    long_words = [word for word in words if len(word) > 5]

    print("Total Words:", word_count)
    print("Total Characters:", char_count)
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Longest Word:", longest_word)
    print("Shortest Word:", shortest_word)
    print("Word Frequency:", dict(freq))
    print("Repeated Words:", repeated_words)
    print("Words Starting with Vowels:", vowel_words)
    print("Words Longer than 5 Characters:", long_words)

# Overall Report
overall_freq = Counter(all_words)

most_used_word = max(overall_freq, key=overall_freq.get)

average_words = total_words / len(messages)

print("\n========== CHAT ANALYTICS REPORT ==========")
print("Most Frequently Used Word:", most_used_word)
print("Longest Message:", longest_message)
print("Shortest Message:", shortest_message)
print("Average Words Per Message:", round(average_words, 2))
print("Complete Word Frequency Dictionary:")
print(dict(overall_freq))