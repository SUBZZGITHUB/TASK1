st=input("enter a string")
print("the string is: ",st)
n=len(st)
print("characters at even index no. are: ")
for i in range(2,n):
    if(i%2==0):
        print('st[',i,']',' - ',st[i])



