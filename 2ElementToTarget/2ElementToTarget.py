a=[]
s=input("Enter a list of number which do not have the same elements:")
for i in s.split(' '):
    a.append(eval(i))
while len(set(a))!=len(a):
    a=[]
    s=input("Enter a list of number which do not have the same elements:")
    for i in s.split(' '):
        a.append(eval(i))

tar=input("Enter the target")
flag=0
for i in a:
    for j in a[a.index(i)+1:]:
        if i+j==tar:
            print(a.index(i),a.index(j))
            flag=1
if flag==0:
    print("No elements can plus to target")


