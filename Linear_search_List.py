pos=-1
def serch (list,n):

    for i in list:
        if list[i]==n:
            globals()['pos']=i
            return True
        return False

#initilization of a List
r=int(input("Range for List"))
list=[]

for i in range(0,r):
    if i<=r:
        i=int(input("Enter Element"))
        list.append(i)
print(list)
a=list
n=int(input("Enter Element to Linear searching"))

if serch(a,n):
    print("Found at", pos+1)

else:
    print("Not found")