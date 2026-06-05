#program to
# Create a list of 20 numbers

numbers = []
print("enter any number 20 :")

for i in range(20):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Original List:", numbers)

# Input number to remove
element = int(input("Enter number to remove: "))
#finding the frequency of given number 
frequency = numbers.count(element)
if frequency == 0:
    print("element not found")
elif frequency == 1:
    print("no duplicates found")
else:
    #reversing the element
    number.reverse()
    for i in range(1,frequency):
        number.remove(element)
    #reversing the list again 
    numbers.remove()
    print("after removing duplicates ")
    print(numbers)