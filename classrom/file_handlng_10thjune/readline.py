Write a program to copy entire content from one file into another

# Open source file in read mode
source = open("source.txt", "r")

# Read entire content
data = source.read()

# Open destination file in write mode
destination = open("destination.txt", "w")

# Copy content
destination.write(data)

print("File copied successfully.")

source.close()
destination.close()