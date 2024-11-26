print("*"*20,"ATM Machine","*"*20)
n=int(input("enter the amount :"))
l=[500,200,100,50,20,10,5,2,1]
temp=0
count=0
for i in l:
    temp=n//i
    print(i,"notes -> ",temp)
    if temp==1:
       count=count+1
       
    n=n%i
print("the no.of single notes",count)
