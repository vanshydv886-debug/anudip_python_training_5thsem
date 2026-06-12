#libary book issue tracker
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

#maxium no ofissues
max_issues = max(book_issues )
print( "max_issues :", max)

#minimum no of issues
min_issues = min(book_issues)
print("min_issues :" , min)



#average no of issues 
average_issues = sum(book_issues) / len(book_issues)
print("average_issues : " , average_issues)

#count of books issued more than 15 times
count = 0

for book in book_issues :
    if book > 15 :
        count += 1
        print(count)

#Books Issued Fewer Than 10 Times: [8, 5] 
 
less_than_10 = []

for issues in book_issues:
    if issues < 10:
        less_than_10.append(issues)

print("Books Issued Fewer Than 10 Times:", less_than_10)
