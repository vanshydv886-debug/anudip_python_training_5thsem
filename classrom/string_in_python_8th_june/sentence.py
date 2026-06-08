#write a program to input a sentence from user and count the no of special character present in the sentnce
n = input("Enter a sentence : ")

count = 0

for ch in sentence :
     if not ch.isalnum() :
       count += 1
print("no of special character",count)