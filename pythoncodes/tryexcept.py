print("enter two numbers:\n")
a=int(input())
b=int(input())
try:
    print("sum of two numbers is:",int(a)+int(b))
except Exception as e:
    print(e)    
