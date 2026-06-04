#program to check whether a number is armstrong or not
num = int(input("enter a number : "))
temp = num   #store the original number for comapr

while temp > 0:  #process last digit
    digit = temp % 10
    sum = sum + (digit**3)
    temp = temp // 10

#result
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an armstrong")
 
