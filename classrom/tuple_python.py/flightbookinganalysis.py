#flight booking analysis
bookings = ( ("P101", "Delhi", "Confirmed"), ("P102", "Mumbai", "Waiting"), ("P103", "Delhi", "Confirmed"), ("P104", "Chennai", "Cancelled"), ("P105", "Mumbai", "Confirmed"), ("P106", "Delhi", "Waiting") )

print("confirmed ticket : ")
for booking in bookings :
    if booking[2] == 'confirmed':
       print(booking[1], booking[2])

#count passenger to delhi
count = 0
for booking in bookings:
    if booking[1] == 'delhi':
        print(booking[0], booking[1])
        count += 1

#Count Confirmed, Waiting, and Cancelled bookings separately
waiting = 0
confirmed = 0
cancelled = 0

for booking in bookings :
    