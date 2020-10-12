#45*3= 555,56+9=77 ,56/6=4

print("\nCALCULATOR.\n")

print("enter two numbers:")
x=int(input())
y=int(input())
print(" press + for ADD\n ,press - for subtract,\n press 3 for /,\n press * for multi\n")
userin=input()

if x==45 and y==3 and userin=="*":
   
    print("45*3=555")
   
elif x==56 and y==9 and userin=="+":
   
    print("56+9=77")
   
elif x==56 and y==6 and userin=="/":
   
    print("56/6=4")
   
elif userin=="*":
   
    print(x,"*",y,"=",x*y)
elif userin=="+":
   
    print(x,"+",y,"=",x+y)    
elif userin=="-":
   
    print(x,"-",y,"=",x-y)
elif userin=="/":
   
    print(x,"/",y,"=",x/y)            
else:
    print("Invalid input.")           

