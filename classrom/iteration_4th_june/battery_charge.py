#program  for displaying battery charging level 
charging_level = 20
while(charging_level<= 100) :    #isme time nhi pt h but battery level ya percent pt h
    if(charging_level):
        print("battery level : " , charging_level, "%")
        charging_level = charging_level + 10
    else:
        break
#------------------------------------------
print("full charge")