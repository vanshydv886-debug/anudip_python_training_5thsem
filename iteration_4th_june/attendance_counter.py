#program for attendance tracker
i = 1
pcount = 0
acount = 0
while(i<=30),
    attendance=input("student " +str(i) + "is present or not(y/n):")
    if attendance="y":
        pcount=pcount+1
        i=i+1
    elif attendance ="n":
        acount=acount+1
        else:
            print("invalid input. please enter 'y' or 'n'.")
print("present students:", pcount)
print("absent sgittudents:", acount)