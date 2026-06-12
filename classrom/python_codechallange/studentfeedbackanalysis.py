#program for student feedback
file = open("feedback.txt", "r")

lines = file.readlines()

# Total lines
total_lines = len(lines)

# Total words
total_words = 0

# Total characters
total_characters = 0

# Vowel count
vowels = "aeiouAEIOU"
vowel_count = 0

for line in lines:
    total_words += len(line.split())
    total_characters += len(line)

    for ch in line:
        if ch in vowels:
            vowel_count += 1

# Longest feedback
longest_feedback = max(lines, key=len).strip()

# Shortest feedback
shortest_feedback = min(lines, key=len).strip()

file.close()

print("Total Lines:", total_lines)
print("Total Words:", total_words)
print("Total Characters:", total_characters)
print("Longest Feedback:", longest_feedback)
print("Shortest Feedback:", shortest_feedback)
print("Total Vowels:", vowel_count)