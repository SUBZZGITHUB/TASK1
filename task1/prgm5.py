beg=int(input("enter the beginning of the interval"))
end=int(input("enter the ending of the interval"))
print("the prime nos. between ",beg,' and ',end,' are: ')
for j in range(beg,end):
    k=0
    for i in range(1,j+1):
        if(j%i==0):
            k=k+1
    if(k==2):
        print(j)
n=int(input("enter the no you want to check for prime "))
k=0
for i in range(1,n+1):
    if(n%i==0):
            k=k+1
if(k==2):
    print(n," is prime")
else:
    print(n," is not prime")




