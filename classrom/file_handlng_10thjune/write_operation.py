Classwork : To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file.

# read data from a file
f = open("sample.txt", "r")

data = f.read()

# Count vowels
vowels = 0
for ch in data.lower():
    if ch in "aeiou":
        vowels += 1

# Count characters
characters = len(data)

# Count lines
lines = len(data.splitlines())

print("Number of vowels =", vowels)
print("Number of characters =", characters)
print("Number of lines =", lines)

f.close()