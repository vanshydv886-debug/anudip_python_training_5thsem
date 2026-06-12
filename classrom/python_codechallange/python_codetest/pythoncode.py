 # Program to count words, lines, and characters in a text file

file = open("text.txt", "r")

content = file.read()

# Count characters
char_count = len(content)

# Count words
word_count = len(content.split())

# Count lines
line_count = len(content.splitlines())

file.close()

print("Total Lines =", line_count)
print("Total Words =", word_count)
print("Total Characters =", char_count