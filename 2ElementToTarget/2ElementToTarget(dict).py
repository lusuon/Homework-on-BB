#dict
a=[]
s=input("Enter a list of number which do not have the same elements:")
for i in s.split(' '):
    a.append(eval(i))
while len(set(a))!=len(a):
    a=[]
    s=input("Enter a list of number which do not have the same elements:")
    for i in s.split(' '):
        a.append(eval(i))
tar=eval(input("Enter the target:"))
flag,b=0,{}
for i in range(len(a)):
    b[a[i]]=i
for i in b.keys():
    for j in b.keys():
        if i+j==tar:
            if b[i]<b[j]:
                print(b[i],b[j])
                flag=1
if flag==0:
    print("No elements can plus to target")
