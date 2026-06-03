#program to check if three angles can form triangle or not
#if yes then specify 
#validate angle1
if(angle1 <= 0):
    exit("Angle must be positive")
#--------------------------------------
angle2 = float(float(input("enter second angle :  ")))
#validate angle2
if(angle2 <=0):
    exit("Angle must be positive")
#---------------------------------------
angle3 = float(input("enter third angle : "))
#validate angles
if(angle3 <= 0):
    exit("Angle must be positive")
#---------------------------------------
#verifying triangle formation
if(angle1 + angle2 + angle3 == 180):
    print("Above angles form a triangle")
    else:
        print("above angles do not form any triangle")