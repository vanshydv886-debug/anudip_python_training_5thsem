#program for student performance analyser
marks = [78, 45, 92, 35, 88, 40, 99, 56]

count = 0
for i in marks:
    if i < 40:
        marks.remove(i)
        count =+1
print("passed  students ", marks)
print("failed students", count)

#highest marks
max = marks[0]
for i in marks:
    if max < i:
        max = i
    else:
        max = max

#lowest marks 
min = marks[0]
for i in marks:
    if min >i:
        min = i
    

print("Highest Marks:", max)
print("Lowest Marks:", mingit )

# Merit List
new_marks = []
for i in marks:
    if i > 75:
        new_marks.append(i)

print("Merit List: ", marks)


