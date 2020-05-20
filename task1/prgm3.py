no=int(input("enter any number"))
num=no
count=0
while(num != 0):
   count=count+1
   num= num // 10
print("total number of digits in ",no,"is: ",count)

