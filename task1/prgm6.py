import math
n=int(input("enter the no of terms you want to print "))
print("the fibonacci series is:")
a,b=0,1
print(a)
print(b)
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c)
no=int(input("enter the no you want to check"))
x=5*no*no + 4
y=5*no*no - 4
sx=int(math.sqrt(x))
sy=int(math.sqrt(y))
if(sx*sx==x or sy*sy==y):
    print(no," is a fibonacci number")
else:
    print(no," is not a fibonacci number")



